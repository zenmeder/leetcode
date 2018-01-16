#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            length = len(nums)
            k %= length
            tmp = nums[:]
            for i in range(k):
                nums[i] = tmp[length-k+i]
            for i in range(k, length):
                nums[i] = tmp[i-k]
        return nums




print(Solution().rotate([1,2,3,4,5,6,7],10))
