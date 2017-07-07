#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def rob(self, nums):
		#动态规划解决
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]
		dp = []
		dp.append(nums[0])
		dp.append(max(nums[0],nums[1]))
		for i in range(2,len(nums)):
			dp.append(max(dp[i-2]+nums[i],dp[i-1]))

		return max(dp)

solution = Solution()
print(solution.rob([1]))
