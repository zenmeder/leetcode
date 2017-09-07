#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def checkPossibility(self, nums):
		count_dec = 0
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				count_dec += 1
				if i == 0:
					nums[i] = nums[i + 1]
				elif nums[i - 1] <= nums[i + 1]:
					nums[i] = nums[i - 1]
				else:
					nums[i + 1] = nums[i]
			if count_dec > 1:
				return False
		return True

