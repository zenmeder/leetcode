#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        s = sum(nums)
        if s % 2: return False
        dp = [True if not _ else False for _ in range(s//2+1)]
        for i in range(len(nums)):
            for j in range(nums[i], s//2+1)[::-1]:
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]

print(Solution().canPartition([3,3,3,4,5]))