cmake_minimum_required(VERSION 3.10)
project(TP4_LowLevel)

# 1. Standard C++ requis
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. Recherche des bibliothèques nécessaires
find_package(cpr REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(Eigen3 REQUIRED)

add_executable(low_level src/main.cpp)

target_link_libraries(low_level 
    PRIVATE 
    cpr::cpr 
    nlohmann_json::nlohmann_json 
    Eigen3::Eigen
)