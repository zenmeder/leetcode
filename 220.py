#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from math import fabs
class Solution(object):
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		if t < 0: return False
		n = len(nums)
		d = {}
		w = t + 1
		for i in range(n):
			m = nums[i] // w
			if m in d:
				return True
			if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
				return True
			if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
				return True
			d[m] = nums[i]
			if i >= k: del d[nums[i - k] // w]
		return False
print(Solution().containsNearbyAlmostDuplicate([4,1,101,3],1,1))