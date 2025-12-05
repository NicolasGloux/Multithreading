# minion.py

import time
import os
import sys

from multiprocessing.managers import BaseManager

from task import Task
from manager import BOSS_IP, BOSS_PORT, AUTH_KEY, STOP_SENTINEL, MyManager 

def run_minion():
    class ClientManager(MyManager): pass 
    ClientManager.register('get_task_queue')
    ClientManager.register('get_result_queue')
    
    while True:
        try:
            manager = ClientManager(address=(BOSS_IP, BOSS_PORT), authkey=AUTH_KEY)
            manager.connect()
            break
        except ConnectionRefusedError:
            time.sleep(2)
        except Exception:
            sys.exit(1)

    q_task = manager.get_task_queue()
    q_result = manager.get_result_queue()
    minion_id = os.getpid()

    while True:
        try:
            task = q_task.get(timeout=10) 

            if task == STOP_SENTINEL:
                q_task.put(STOP_SENTINEL) 
                break

            task.work() 

            result = f"Tâche {task.identifier} terminée par Minion {minion_id} en {task.time:.4f}s."
            
            q_result.put(result)

        except TimeoutError:
             continue
        except Exception:
            break


if __name__ == '__main__':
    run_minion()
