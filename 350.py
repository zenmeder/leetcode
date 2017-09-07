#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		a = Counter(nums1)
		result = []
		for num in nums2:
			if num in a and a[num]:
				result.append(num)
				a[num] -= 1
		return result

print(Solution().intersect([1],[1,1]))
