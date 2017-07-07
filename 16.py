#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def threeSumClosest(self, nums, target):
		length = len(nums)
		if length < 3:
			return 'Failed'
		nums.sort()
		for i in range(length - 2):
			if i != 0 and nums[i] == nums[i - 1]:
				continue
			j = i + 1
			k = length - 1
			while j < k:
				temp_distance = nums[i] + nums[j] + nums[k] - target
