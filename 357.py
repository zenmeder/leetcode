#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math

class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0,0,9]
		if n <=2 :
			return int(pow(10,n))-dp[n]
		for i in range(3,n+1):
			dp.append(dp[-1]*10+(9*int(pow(10,i-2))-dp[-1])*(i-1))
		print(dp)
		return int(pow(10,n))-sum(dp)



print(Solution().countNumbersWithUniqueDigits(4))
