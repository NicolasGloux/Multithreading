# boss.py

import time
import random
import sys

from multiprocessing.managers import BaseManager

from task import Task
from manager import BOSS_IP, BOSS_PORT, AUTH_KEY, STOP_SENTINEL, MyManager 

NUM_MINIONS_EXPECTED = 3 
NUM_TASKS = 10 

def boss_orchestration():
    class ClientManager(MyManager): pass 
    ClientManager.register('get_task_queue')
    ClientManager.register('get_result_queue')
    
    manager = ClientManager(address=(BOSS_IP, BOSS_PORT), authkey=AUTH_KEY)

    try:
        manager.connect()
    except ConnectionRefusedError:
        sys.exit(1)

    q_task = manager.get_task_queue()
    q_result = manager.get_result_queue()
    
    for i in range(1, NUM_TASKS + 1):
        task_size = random.randint(100, 500) 
        task = Task(identifier=i, size=task_size) 
        q_task.put(task)

    start_time = time.time()
    for i in range(NUM_TASKS):
        result = q_result.get()
        
    print(f"\nBoss: Toutes les tâches ont été traitées en {time.time() - start_time:.2f}s.")
    
    for _ in range(NUM_MINIONS_EXPECTED):
        q_task.put(STOP_SENTINEL) 

if __name__ == '__main__':
    boss_orchestration()
