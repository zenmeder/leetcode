#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from itertools import combinations

class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		return list(combinations(range(1, n+1), k))

print(Solution().combine(4,2))