#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        m, n = float('-inf'), float('inf')
        for i in range(length):
            m = max(m, nums[i])
            n = min(n, nums[i])
        capacity = (m - n) // length + 1
        counts = (m - n) // capacity + 1
        buckets = [[] for i in range(counts)]
        for i in range(length):
            buckets[(nums[i]-n)//capacity].append(nums[i])
        buckets = [bucket for bucket in buckets if bucket]
        res = 0
        for i in range(len(buckets)-1):
            res = max(res, min(buckets[i+1])-max(buckets[i]))
        return res
print(Solution().maximumGap([40, 62, 42, 81, 43, 67, 32, 95, 53, 88]))
