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
        dp, m, n= [1] * len(nums), 1, 1,
        for i in range(1, len(nums)):
            if m == 1:
                n += 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[j] + 1 == m:
                        n += 1
                    elif dp[j] + 1 > m:
                        m = dp[j] + 1
                        n = 1
            print(i,m,n)
        print(dp)
        return m,n



print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))
