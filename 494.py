#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findTargetSumWays(self, nums, S):
		if not nums:
			return 0
		for i in range(len(nums)):
			if i == 0:
				dp = {nums[0]: 1, -nums[0]: 1} if nums[0] else {0:2}
				continue
			now = {}
			for pre in dp.keys():
				now[pre + nums[i]] = dp[pre] if pre + nums[i] not in now else now[pre + nums[i]] + dp[pre]
				now[pre - nums[i]] = dp[pre] if pre - nums[i] not in now else now[pre - nums[i]] + dp[pre]
			dp = now
		return dp[S] if S in dp else 0

print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1],1))