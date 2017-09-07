#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findSubsequences(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if not nums or len(nums) < 2:
			return []
		dps = [[[nums[0]]]]
		for i in range(1, len(nums)):
			tdp = dps[-1][:]
			tdp.append([nums[i]])
			for dp in dps[-1]:
				if nums[i] >= dp[-1]:
					tdp.append(dp+[nums[i]])
			dps.append(tdp)
		res = (tuple(i) for i in dps[-1] if len(i)>1)
		return list(set(res))
print(Solution().findSubsequences([4, 6, 7, 7]))