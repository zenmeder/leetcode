#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp, times = [1], [1]
        for i in range(1,len(nums)):
            m, n = 1, 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > m:
                        m = dp[j] + 1
                        n = times[j]
                    elif dp[j] + 1 == m:
                        n += times[j]
            dp.append(m)
            times.append(n)
        maxLength = max(dp)
        return sum([times[_] for _ in range(len(nums)) if dp[_] == maxLength])



print(Solution().findNumberOfLIS([1,3,5,4,7]))
