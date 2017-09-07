#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		d = {}
		while n != 1:
			n = str(n)
			sum = 0
			for i in range(len(n)):
				sum += int(n[i]) ** 2
			if sum in d:
				return False
			else:
				d[sum] = 1
			n = sum
		return True
print(Solution().isHappy(3))