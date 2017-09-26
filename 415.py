#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		if not num1 or not num2:
			return num1 + num2
		if len(num1) > len(num2):
			num1, num2 = num2, num1
		num1 = '0'*(len(num2)-len(num1)) + num1
		pre , res = 0, ''
		for i in range(len(num1))[::-1]:
			res = str((int(num1[i]) + int(num2[i]) + pre) % 10) + res
			pre = (int(num1[i]) + int(num2[i]) + pre) // 10
		return res if not pre else '1'+res

print(Solution().addStrings('99','1'))