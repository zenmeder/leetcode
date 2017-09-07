#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import numpy as np
class Solution(object):
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""
		if not nums or not nums[0] or r * c != len(nums) * len(nums[0]):
			return nums
		#直接用numpy的reshape函数
		#return [list(l) for l in np.array(nums).reshape(r,c)]
		result = []
		l = []
		for i in range(len(nums)):
			for j in range(len(nums[i])):
				l.append(nums[i][j])
				if len(l) == c:
					result.append(l)
					l = []
		return result


print(Solution().matrixReshape([[1,2],
 [3,4]], 1,4))