#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d1 = {} #store
        self.d2 = [] #to be evict

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d1:


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """



        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)