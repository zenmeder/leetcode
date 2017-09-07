#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		stop = []
		maxL = 0
		for i in range(len(nums)):
			zeros, ones, crt = 0, 0, 0
			if not stop or stop[-1] == 0:
				for j in range(i, len(nums)):
					if nums[j]:
						ones += 1
					else:
						zeros += 1
					if ones == zeros:
						crt = ones
						maxL = max(maxL, 2*crt)
				stop.append(crt)
			else:
				zeros, ones = stop[-1], stop[-1]
				crt = 0
				if nums[i-1]:
					ones -= 1
				else:
					zeros -= 1
				for j in range(i+2*stop[-1], len(nums)):
					if nums[j]:
						ones += 1
					else:
						zeros += 1
					if ones == zeros:
						crt = ones
						maxL = max(maxL, 2*crt)
				stop.append(crt)
		print(stop)
		return maxL

print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))