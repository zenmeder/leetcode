#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		a = Counter(nums1)
		result = []
		for num in nums2:
			if num in a :
				result.append(num)
				a.pop(num)
		return result

print(Solution().intersection([1,2,2],[2,2]))