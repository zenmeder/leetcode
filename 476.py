#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		return 2 ** (len(bin(num)[2:])) - num - 1

print(Solution().findComplement(19))
