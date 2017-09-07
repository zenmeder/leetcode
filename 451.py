#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution(object):
	def frequencySort(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		fre = Counter(s).most_common()
		res = ''.join([a[0]*a[1] for a in fre])
		return res

print(Solution().frequencySort(''))

