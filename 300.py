#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	# dp O(n^2)
	def lengthOfLIS(self, nums):
		if not nums: return 0
		dp, length, res = [1], len(nums), 1
		for i in range(1, length):
			ml = 1
			for j in range(i):
				if nums[j] <= nums[i]:
					ml = max(ml, 1 + dp[j])
			res = max(res, ml)
			dp.append(ml)
		return res

print(Solution().lengthOfLIS([]))