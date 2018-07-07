import unittest
import queue

class QueueTwoStacks(object):
    stack1 = queue.LifoQueue()
    stack2 = queue.LifoQueue()

    def enqueue(self, item):
        self.stack1.put(item)

    def dequeue(self):
        if(self.stack1.qsize()==0):
            raise Exception("queue empty")
        else:
            while(self.stack1.qsize()>1):
                self.stack2.put(self.stack1.get())
            temp = self.stack1.get()
            while(self.stack2.qsize()>0):
                self.stack1.put(self.stack2.get())
            return temp


# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)