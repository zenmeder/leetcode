#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = None
        for i, num in enumerate(nums):
            if num == 0 and first == None:
                first = i
                continue
            if num != 0 and first != None:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
        return nums

print(Solution().moveZeroes([1]))