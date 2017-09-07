#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n > 0 and int(math.log10(n) / math.log10(3)) - math.log10(n) / math.log10(3) == 0:
			return True
		return False

print(Solution().isPowerOfThree(23))
