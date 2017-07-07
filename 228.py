#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		p = 0
		result = []
		while p < len(nums):
			if p == len(nums) - 1:
				result.append(str(nums[-1]))
				break
			q = p + 1
			while (q < len(nums)) and (nums[q]-1 == nums[q - 1]):
				q += 1
			if q == p+1:
				result.append(str(nums[p]))
			else:
				result.append("{}->{}".format(nums[p],nums[q-1]))
			p = q
		return result
solution = Solution()
print(solution.summaryRanges([0,2,4]))