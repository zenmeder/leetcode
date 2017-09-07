#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def kSmallestPairs(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[List[int]]
		"""
		p = [0] * len(nums1)
		count = 0
		res = []
		while count < k and count < len(nums1) * len(nums2):
			small = None
			print(p)
			for i, x, y in zip([i for i in range(len(nums1))], nums1, p):
				if y == len(nums2):
					continue
				elif small == None or small > x + nums2[y]:
					small = x + nums2[y]
					mark = i
			res.append([nums1[mark], nums2[p[mark]]])
			p[mark] += 1
			count += 1
		return res


print(Solution().kSmallestPairs([-10, -4, 0, 0, 6], [3, 5, 6, 7, 8, 100], 10))
