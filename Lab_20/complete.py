import threading
from queue import Queue
import time

def producer(q):
    for i in range(6):
        time.sleep(1)
        item = f'Item {i}'
        q.put(item)
        print(f'Produced {item}')

def consumer(q):
    while True:
        item = q.get()
        time.sleep(2)
        print(f'Consumed {item}')
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()

    # wait for both threads to complete
    t1.join()
    t2.join()

    # wait for all tasks in the queue to be completed
    q.join()