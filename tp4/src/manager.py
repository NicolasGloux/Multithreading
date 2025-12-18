from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import sys

BOSS_IP = 'localhost' 
BOSS_PORT = 50000
AUTH_KEY = b'abracadabra'

TASK_QUEUE = Queue()
RESULT_QUEUE = Queue()

class MyManager(BaseManager):
    pass

class QueueClient:
    def __init__(self):
        MyManager.register('get_task_queue')
        MyManager.register('get_result_queue')
        self.m = MyManager(address=(BOSS_IP, BOSS_PORT), authkey=AUTH_KEY)
        self.m.connect()
        self.task_queue = self.m.get_task_queue()
        self.result_queue = self.m.get_result_queue()

def start_manager_server():
    MyManager.register('get_task_queue', callable=lambda: TASK_QUEUE)
    MyManager.register('get_result_queue', callable=lambda: RESULT_QUEUE)
    manager = MyManager(address=(BOSS_IP, BOSS_PORT), authkey=AUTH_KEY)
    try:
        print(f"Manager lancé sur {BOSS_IP}:{BOSS_PORT}")
        server = manager.get_server()
        server.serve_forever()
    except Exception:
        sys.exit(1)

if __name__ == '__main__':
    start_manager_server()
