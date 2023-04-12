# Cesar Almendarez
# CSULA Spring 2023
# CS 3035-01 Programming Paradigms
# Lab 20(Concurrency)
# April 11 2023

from queue import Queue
from threading import Thread
import time  

# producer():
#   in for loop:
#       sleep for 1s
#       insert item in queue
#       print item inserted
def producer(test_queue):
    for i in range(6):
        time.sleep(1)

        # Initialize new queue
        item = "Item {}".format(i)

        # Insert item into queue
        test_queue.put(item)

        print("Inserted " + item)
        
# consumer():
#   get item from queue
#   sleep for 2s
#   print the item processed
def consumer(test_queue):
    while True:
        # Get produced item
        item = test_queue.get()

        # Process every 2 seconds with tim.sleep()
        time.sleep(2)

        print("Processed " + item)

        test_queue.task_done()

# main function
if __name__ == "__main__":
    test_queue = Queue()    

    # Initialize threads 
    thread_1 = Thread(target = producer, args = (test_queue, ))
    thread_2 = Thread(target = consumer, args = (test_queue, ))

    # Start threads
    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    test_queue.join()

# Output
# Inserted Item 0
# Inserted Item 1
# Processed Item 0
# Inserted Item 2
# Inserted Item 3
# Processed Item 1
# Inserted Item 4
# Inserted Item 5
# Processed Item 2
# Processed Item 3
# Processed Item 4
# Processed Item 5