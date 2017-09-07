#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		k = k - len(nums) if k > len(nums) else k
		nums = nums[-k:] + nums[0:len(nums) - k]
		print(nums)

print(Solution().rotate([1, 2], 1))
