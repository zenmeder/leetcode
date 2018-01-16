#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MyCalendarTwo:
    def __init__(self):
        self.c = {}
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

a = MyCalendarTwo()
print(a.book(10,20))
print(a.book(50,60))
print(a.book(10,40))
print(a.book(5,15))
print(a.book(5,10))
print(a.book(25,55))