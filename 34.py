#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def searchRange(self, nums, target):
		low = 0
		high = len(nums)
		while True:
			mid = int((low + high) / 2)
			# print(low,high,mid)
			if low >= high:
				break
			else:
				if nums[mid] < target:
					low = mid + 1
				elif nums[mid] > target:
					high = mid - 1
				else:
					break
		if mid == len(nums) or nums[mid] != target:
			return [-1, -1]
		else:
			start = stop = mid
			while start != -1:
				if nums[start] == nums[mid]:
					start -= 1
				else:
					break
			while stop != len(nums):
				if nums[stop] == nums[mid]:
					stop += 1
				else:
					break
			return [start+1,stop-1]
				# while nums[start] == nums[mid] or nums[stop] == nums[mid] or (start == 0 and stop == len(nums)):
				# 	if start != 0 and nums[start] == nums[mid]:
				# 		start -= 1
				# 	if stop != len(nums) and nums[stop] == nums[mid]:
				# 		stop += 1
				# return [start+1, stop-1]


solution = Solution()
print(solution.searchRange([i for i in range(1000)], 5))
