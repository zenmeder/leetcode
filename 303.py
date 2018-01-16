#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d, a = {}, 0
        for i in range(len(nums)):
            a += nums[i]
            self.d[i] = a

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.d[j] - self.d[i-1] if i != 0  else self.d[j]
