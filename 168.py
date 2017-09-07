#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		result = []
		while True:
			if 1<=n<=26:
				result.append(chr(n+64))
				break
			if n % 26 == 0:
				result.append('Z')
			else:
				result.append(chr(n%26+64))
			n //= 26

		return ''.join(result[::-1])

print(Solution().convertToTitle(52))
