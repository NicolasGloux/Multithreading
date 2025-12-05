# manager.py

from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import time
import sys

BOSS_IP = 'localhost' 
BOSS_PORT = 50000
AUTH_KEY = b'abracadabra'
STOP_SENTINEL = 'STOP'

TASK_QUEUE = Queue()
RESULT_QUEUE = Queue()

class MyManager(BaseManager):
    pass

def start_manager_server():
    MyManager.register('get_task_queue', callable=lambda: TASK_QUEUE)
    MyManager.register('get_result_queue', callable=lambda: RESULT_QUEUE)
    
    manager = MyManager(address=(BOSS_IP, BOSS_PORT), authkey=AUTH_KEY)
    
    try:
        server = manager.get_server()
        server.serve_forever()
    except Exception as e:
        sys.exit(1)

if __name__ == '__main__':
    start_manager_server()
