#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def searchInsert(self, nums, target):
		low = 0
		high = len(nums)-1
		while low<=high:
			mid = int((low+high)/2)
			if nums[mid] == target:
				return mid
			elif nums[mid]<target:
				low = mid+1
			else:
				high = mid-1
		return high+1

solution = Solution()
print(solution.searchInsert([0,2,4,6,8],-1))