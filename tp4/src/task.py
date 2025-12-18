# task.py (Mise à jour complète avec JSON et Égalité)

import time
import numpy as np
import json # Nouveau module requis

class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        self.size = size or np.random.randint(300, 3_000)
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    # --- TP 3: Sérialisation ---

    def to_json(self) -> str: # 
        """Sérialise l'objet Task en une chaîne JSON."""
        data = {
            "identifier": self.identifier,
            "size": self.size,
            # Convertit les tableaux NumPy en listes Python standard pour JSON
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time
        }
        return json.dumps(data)

    @staticmethod
    def from_json(text: str) -> "Task": # [cite: 180, 181]
        """Crée un objet Task à partir d'une chaîne JSON."""
        data = json.loads(text)
        
        # Créer une nouvelle instance de Task (le __init__ est ignoré)
        task = Task()
        
        # Remplir les attributs avec les données désérialisées
        task.identifier = data["identifier"]
        task.size = data["size"]
        
        # Reconvertir les listes en tableaux NumPy
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        
        task.time = data["time"]
        
        return task

    # --- TP 3: Égalité ---

    def __eq__(self, other: "Task") -> bool: # 
        """Définit l'égalité entre deux objets Task."""
        if not isinstance(other, Task):
            return NotImplemented
        
        # Vérifie l'égalité de tous les attributs
        if self.identifier != other.identifier or \
           self.size != other.size or \
           self.time != other.time:
            return False
            
        # Utilise np.array_equal pour comparer les tableaux NumPy (plus précis)
        if not np.array_equal(self.a, other.a) or \
           not np.array_equal(self.b, other.b) or \
           not np.array_equal(self.x, other.x):
            return False
            
        return True
