#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.d[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for key in self.d.keys():
            if key.startswith(prefix):
                res += self.d[key]
        return res