#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import heapq
class Solution(object):
	def findKthNumber(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: int
		"""
		strs = sorted([str(s) for s in range(1, n+1)], key=lambda x: str(x))
		hq = heapq.heapify(strs)
		i = 0
		while i<k:
			res = next(hq)
			i+=1
		return res

print(Solution().findKthNumber(13,2))
