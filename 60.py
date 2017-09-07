#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math

from itertools import permutations
class Solution(object):
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		# if k > math.factorial(n):
		# 	return ''
		# a1 = k // (math.factorial(n - 1))
		# # print(k,(math.factorial(n - 1)) )
		# nums = [i for i in range(1,n+1)]
		# nums.remove(a1)
		# return nums
		a = permutations(range(1,n+1))
print(Solution().getPermutation(3,2))