#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def checkSubarraySum(self, nums, k):
		for i in range(len(nums)):
			sums = nums[i]
			for j in range(i + 1, len(nums)):
				sums += nums[j]
				if k==0 and sums==0:
					return True
				elif k==0 and sums!=0:
					continue
				elif sums % k == 0:
					return True
		return False


solution = Solution()
print(solution.checkSubarraySum([23,2,6,4,7], 0))
