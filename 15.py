#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import time


class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		result = []
		for i in range(len(nums) - 2):
			if i != 0 and nums[i] == nums[i - 1]:
				continue
			j = i + 1
			k = len(nums) - 1
			while j<k:
				sum = nums[i]+nums[j]+nums[k]
				if sum < 0:
					j+=1
					continue
				elif sum > 0:
					k-=1
					continue
				else:
					result.append([nums[i],nums[j],nums[k]])
					j += 1
					k -= 1
					while j < k and nums[j] == nums[j - 1]:
						j += 1
					while j < k and nums[k] == nums[k + 1]:
						k -= 1
		return result




p = time.clock()
solution = Solution()
print(solution.threeSum([0,0,0,0,0,0,0,0,0]))
print(time.clock() - p)
