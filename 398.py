#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import bisect, random
class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = sorted(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        i, j = bisect.bisect_left(self.nums, target), bisect.bisect_right(self.nums, target)-1
        return random.randint(i, j)
print(Solution([1,2,3,3,3]).pick(3))

