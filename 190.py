#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		result = 0
		for i in range(32):
			if n&1 == 1:
				result = (result<<1)+1
			else:
				result <<= 1
			n>>=1
		return result
solution = Solution()
print(solution.reverseBits(43261596))