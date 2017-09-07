#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num == 0:
			return False
		if len(bin(num)) % 2 and not (num & num-1):
			return True
		return False


print(Solution().isPowerOfFour(1))
