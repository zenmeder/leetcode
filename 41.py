#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def firstMissingPositive(self, nums):
		length = len(nums)
		d = dict()
		max_num = 0
		for i in range(length):
			if nums[i] <= 0:
				continue
			d[nums[i]] = 1
			max_num = max(max_num,nums[i])
		if not d:
			return 1
		for i in range(1,max_num):
			if i not in d:
				return i
		return max_num+1
solution = Solution()
print(solution.firstMissingPositive([1]))
