#include <iostream>
#include <vector>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
#include <Eigen/Dense>

using json = nlohmann::json;

int main() {
    // 1. Création de données avec Eigen
    int size = 3;
    Eigen::MatrixXd matrixA = Eigen::MatrixXd::Random(size, size);
    Eigen::VectorXd vectorB = Eigen::VectorXd::Random(size);

    // 2. Préparation du JSON pour task.py
    std::vector<std::vector<double>> a_list;
    for (int i = 0; i < matrixA.rows(); ++i) {
        a_list.push_back(std::vector<double>(matrixA.row(i).data(), matrixA.row(i).data() + matrixA.cols()));
    }
    std::vector<double> b_list(vectorB.data(), vectorB.data() + vectorB.size());

    json task_json;
    task_json["identifier"] = 42;
    task_json["size"] = size;
    task_json["a"] = a_list;
    task_json["b"] = b_list;
    task_json["x"] = std::vector<double>(size, 0.0);
    task_json["time"] = 0.0;

    // 3. Envoi au Proxy HTTP (port 8000)
    std::string url = "http://localhost:8000";
    std::cout << "Envoi de la tâche au proxy..." << std::endl;

    auto response = cpr::Post(
        cpr::Url{url},
        cpr::Body{task_json.dump()},
        cpr::Header{{"Content-Type", "application/json"}}
    );

    // 4. Affichage du résultat
    if (response.status_code == 200) {
        std::cout << "Succès ! Le proxy a répondu : " << response.text << std::endl;
    } else {
        std::cerr << "Erreur " << response.status_code << " : " << response.error.message << std::endl;
    }

    return 0;
}