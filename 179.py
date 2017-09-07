#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution:
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		if nums == [0]*len(nums):
			return '0'
		nums = [str(i) for i in nums]
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] < nums[j] + nums[i]:
					nums[i], nums[j] = nums[j], nums[i]

		return ''.join(nums)

print(Solution().largestNumber([3, 30, 34, 5, 9]))
