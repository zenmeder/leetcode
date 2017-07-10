#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# curSum = result = nums[0]
		curSum = 0
		result = None
		for i in range(0,len(nums)):
			if curSum < 0:
				curSum = 0
			curSum = curSum+nums[i]
			if result == None:
				result = curSum
			result = max(result,curSum)
		return result
solution = Solution()
print(solution.maxSubArray([-2147483647]))
