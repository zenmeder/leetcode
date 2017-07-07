#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: list
		"""
		if len(nums) == 1:
			return 1
		count = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i-1]:
				nums[count] = nums[i]
				count+=1
		return nums[:i]
solution = Solution()
print(solution.removeDuplicates([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]))