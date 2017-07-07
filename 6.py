#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if len(s) <= numRows:
			return s
		if numRows == 1:
			return s
		result = ''
		maxZigZag = int(len(s) / (numRows + 1))
		if len(s) > maxZigZag * (numRows + 1):
			maxZigZag += 1
		flag = True
		if numRows == 2:
			maxZigZag = int(len(s) / numRows)
			if len(s) > maxZigZag * numRows:
				maxZigZag += 1
			for i in range(2):
				for j in range(maxZigZag):
					if 2*j+i < len(s):
						result += s[2*j+i]
			return result
		for i in range(numRows):
			for j in range(maxZigZag):
				if numRows % 2:
					if i != (numRows - 1) / 2 and ((numRows + 1) * j + i < len(s)):
						result += s[(numRows + 1) * j + i]
					elif i == (numRows - 1) / 2 and ((numRows + 1) * j + i < len(s)):
						result += s[(numRows + 1) * j + i]
						if ((numRows + 1) * (j + 1) - 1 < len(s)):
							result += s[(numRows + 1) * (j + 1) - 1]
				else:
					if i == numRows / 2 and flag:
						for k in range(maxZigZag):
							if (numRows + 1) * (k + 1) - 1 < len(s):
								result += s[(numRows + 1) * (k + 1) - 1]
								flag = False
					if (numRows + 1) * j + i < len(s):
						result += s[(numRows + 1) * j + i]
						print(result)
		return result


solution = Solution()
print(solution.convert("ABC", 2))
