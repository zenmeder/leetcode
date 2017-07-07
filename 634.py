#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math
class Solution(object):
	def findDerangement(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n==1:
			return 0
		if n==2:
			return 1
		if n==3:
			return 2
		if n==4:
			return 9
		a = [0,0,0,1,3]
		for i in range(5,n+1):
			x = ((i-2)*a[i-1])%1000000007
			y = ((i-3)*a[i-2])%1000000007
			a.append((x+y)%1000000007)
		return ((n-1)*a[-1])%(1000000007)

solution = Solution()
print(solution.findDerangement(2321300))