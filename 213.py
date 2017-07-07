#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def rob(self, nums):
		# relative problem 198
		# 分别去掉第一个和最后一个元素求最大的可能偷窃金额，再取二者中的大的
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			return nums[0]
		if length == 2:
			return max(nums)
		return max(self.robMoney(nums,0,length-1),self.robMoney(nums,1,length))
	def robMoney(self, nums, begin, end):
		dp = []
		dp.append(nums[begin])
		dp.append(max(nums[begin],nums[begin+1]))
		for i in range(begin+2,end):
			# print()
			dp.append(max(nums[i]+dp[i-2-begin],dp[i-1-begin]))
		return max(dp)

solution = Solution()
print(solution.rob([0,0,0]))