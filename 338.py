#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from collections import Counter
class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		res = []
		for i in range(num+1):
			a = bin(i)[2:]
			res.append(Counter(a)['1'])
		return res

print(Solution().countBits(100))