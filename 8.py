#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		str = str.lstrip()
		i = 0
		result = ''
		int_max = 2**31-1
		int_min = -2**31
		while i < len(str):
			if '0' <= str[i] <= '9' or str[i] == '+' or str[i] == '-':
				result += str[i]
				i += 1
				continue
			break
		try:
			result = int(result)
			if result > int_max:
				return int_max
			elif result < int_min:
				return int_min
			else:
				return result
		except:
			return 0
print(Solution().myAtoi("  -0012a42"))
