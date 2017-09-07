#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: list
		"""
		if not nums:
			return 0
		slow = fast = i = 0
		while fast < len(nums):
			while fast < len(nums) and nums[fast] == nums[slow]:
				fast += 1
			nums[i] = nums[slow]
			i += 1
			slow = fast
		return nums[:i]


solution = Solution()
print(solution.removeDuplicates([1]))
