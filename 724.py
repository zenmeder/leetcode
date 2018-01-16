#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = [], []
        a, b = 0, sum(nums)
        for i in range(len(nums)):
            b -= nums[i]
            left.append(a)
            right.append(b)
            a += nums[i]
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1

print(Solution().pivotIndex([-1,1,2]))