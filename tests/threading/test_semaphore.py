from queue import Queue
from threading import Semaphore, Thread
from unittest import TestCase


class Task(Thread):
    def __init__(self, semaphore: Semaphore, queue: Queue):
        super().__init__()
        self.semaphore = semaphore
        self.queue = queue

    def run(self):
        self.semaphore.acquire()
        for i in range(0, 10):
            self.queue.put((self.name, i))
        self.semaphore.release()


class SemaphoreTest(TestCase):
    def test(self):
        semaphore = Semaphore(2)
        queue = Queue()

        tasks = []
        for i in range(4):
            t = Task(semaphore, queue)
            tasks.append(t)

        for t in tasks:
            t.start()

        for t in tasks:
            t.join()

        # 後半のスレッドはセマフォでブロックされることを確認する
        thread_names = [queue.get()[0] for _ in range(40)]
        first_20_names = set(thread_names[:20])
        last_20_names = set(thread_names[20:])

        self.assertEqual(2, len(first_20_names))
        self.assertEqual(2, len(last_20_names))
        self.assertEqual(0, len(first_20_names & last_20_names))
