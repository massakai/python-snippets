#!/usr/bin/python

import threading
import time

class Task(threading.Thread):
    def __init__(self, sem):
        threading.Thread.__init__(self)
        self.semaphore = sem
    
    def run(self):
        self.semaphore.acquire()
        for i in range(0, 10):
            print "%s: %d" % (self.name, i)
            time.sleep(0.1)
        self.semaphore.release()

if __name__ == '__main__':
    semaphore = threading.Semaphore(8)
    
    tasks = []
    for i in range(0, 20):
        t = Task(semaphore)
        t.start()
        tasks.append(t)

    for t in tasks:
        t.join()

    print 'all tasks joined.'
