#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import defaultdict
class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		if not nums:
			return False
		d = defaultdict(list)
		for i in range(len(nums)):
			if nums[i] not in d:
				d[nums[i]] = [i]
			elif i-d[nums[i]][-1] <=k:
				return True
			else:
				d[nums[i]].append(i)
		return False

print(Solution().containsNearbyDuplicate([1,1],3))


