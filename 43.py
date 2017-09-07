#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		res = 0
		m, n = len(num1), len(num2)
		for i in range(m)[::-1]:
			for j in range(n)[::-1]:
				res += int(num1[i]) * int(num2[j]) * 10**(m+n-2-i-j)
		return str(res)

print(Solution().multiply('123209849028904','1283240'))