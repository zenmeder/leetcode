#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findKthNumber(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: int
		"""
		strs = [str(s) for s in range(1, n+1)]
		strs = sorted(strs, key=lambda x: str(x))
		print(strs)
		return strs[k-1]

print(Solution().findKthNumber(4289384,1922239))
