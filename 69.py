#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def mySqrt(self, x):
		# 牛顿迭代法
		if x == 0 or x == 1:
			return x
		if x == 1:
			return True
		i = 1
		j = x - 1
		while i <= j:
			mid = (i + j) // 2
			if mid ** 2 == x:
				return mid
			elif mid ** 2 > x:
				j = mid - 1
				continue
			elif mid ** 2 < x:
				i = mid + 1
				continue
		return i if i**2<x else i-1


print(Solution().mySqrt(1))
