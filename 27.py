#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        def findNext(p):
            for i in range(p, length):
                if nums[i] != val:
                    return i
            return -1
        for i in range(length):
            if nums[i] == val:
                n = findNext(i)
                if n == -1:
                    return i
                else:
                    nums[i], nums[n] = nums[n], nums[i]
print(Solution().removeElement([3,2,3,2],3))


