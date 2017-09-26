#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, res = 0, 0
        for i in range(len(nums)):
            if not i:
                dp = 1
                res = 1
                continue
            dp = dp + 1 if nums[i] > nums[i - 1] else 1
            res = res if res >= dp else dp
        return res


print(Solution().findLengthOfLCIS([]))
