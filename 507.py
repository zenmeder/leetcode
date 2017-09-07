#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from math import sqrt

class Solution(object):
	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 0:
			return False
		divisors = set()
		for i in range(1, int(sqrt(num))+1):
			if not num % i:
				divisors.add(i)
				divisors.add(num//i)
		divisors.remove(num)
		return num==sum(divisors)

print(Solution().checkPerfectNumber(28))
