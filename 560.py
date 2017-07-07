#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def subarraySum(self, nums, k):
		count = 0
		for i in range(len(nums)):
			sums = nums[i]
			if sums == k:
				count += 1
			for j in range(i+1,len(nums)):
				sums += nums[j]
				if sums == k :
					count += 1
		return count

solution = Solution()
print(solution.subarraySum([1,2,3],3))