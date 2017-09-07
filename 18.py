#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		print(nums)
		result = []
		for i in range(len(nums) - 3):
			if i != 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, len(nums) - 2):
				if j != i + 1 and nums[j] == nums[j - 1]:
					continue
				k = j + 1
				l = len(nums) - 1
				while k < l:
					sums = nums[i] + nums[j] + nums[k] + nums[l] - target
					if sums == 0:
						result.append([nums[i] , nums[j] , nums[k] , nums[l]])
						k += 1
						l -= 1
						while k < l and nums[k] == nums[k - 1]:
							k += 1
						while k < l and nums[l] == nums[l + 1]:
							l -= 1
					elif sums > 0:
						l -= 1
						continue
					elif sums < 0:
						k += 1
						continue
		return result


print(Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9))
