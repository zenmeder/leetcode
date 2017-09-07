#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def convertToBase7(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		num = str(num)
		positive = 1
		if num[0] == '-':
			positive = 0
			num = int(num[1:])
		else:
			num = int(num)
		quotients = num//7
		remainder = []
		remainder.append(str(num % 7))
		while quotients > 0:
			num = quotients
			quotients = num//7
			remainder.append(str(num % 7))
		if positive:
			return ''.join(remainder[::-1])
		else:
			return '-'+''.join(remainder[::-1])

print(Solution().convertToBase7(10))