#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MyCalendar:
    def __init__(self):
        self.s = []
        self.e = []
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        p = self.find(start, end)
        if p == -1:
            return False
        self.s.insert(p, start)
        self.e.insert(p, end)
        return True

    def find(self, start, end):
        if not self.s:
            return 0
        low, high = 0, len(self.s)-1
        while low <= high:
            mid = (low + high) // 2
            if self.e[mid] < start:
                low = mid + 1
            elif self.e[mid] > start:
                high = mid - 1
            else:
                low = mid + 1
                break
        if low == len(self.s) or self.s[low] >= end:
            return low
        return -1

b = MyCalendar()
print(b.book(0,6))
print(b.book(6,14))
print(b.book(6,11))
print(b.e)
print(b.s)