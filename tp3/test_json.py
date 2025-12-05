# test_json.py

import unittest
from task import Task

class TestTaskSerialization(unittest.TestCase):
    
    def test_serialization_equality(self):
        """
        Instancie Task a, la sérialise, la désérialise en Task b, 
        et vérifie que a == b.
        """
        # 1. Instancie une première tâche (a) 
        # Nous appelons work() pour remplir self.x et self.time, 
        # garantissant que tous les champs sont testés.
        a = Task(identifier=101, size=20)
        a.work() 
        
        # 2. Sérialise la première tâche 
        txt = a.to_json()
        
        # 3. Désérialise pour obtenir la seconde tâche (b) 
        b = Task.from_json(txt)
        
        # 4. S'assure que a est égal à b 
        self.assertEqual(a, b, "L'objet désérialisé n'est pas égal à l'objet original.")

if __name__ == '__main__':
    unittest.main()
