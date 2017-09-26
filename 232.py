#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = list()
        self.low = 0
        self.high = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.q.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        res = self.q[self.low]
        self.low += 1
        return res
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.q[self.low]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.low == len(self.q):
            return True
        return False

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
q.pop()
print(q.peek())
q.pop()
print(q.empty())


        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()