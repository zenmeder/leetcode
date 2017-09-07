#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findMaxAverage(self, nums, k):
		if not nums:
			return 0
		if k >= len(nums):
			return sum(nums) / len(nums)
		count = sum(nums[0:k])
		maxCount = count
		# print(count)
		for i in range(1, len(nums) - k + 1):
			count = count - nums[i - 1] + nums[k - 1 + i]
			maxCount = max(maxCount, count)
		return maxCount / float(k)


print(Solution().findMaxAverage([0, 4, 0, 3, 2], 1))
