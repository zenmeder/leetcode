#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def largestPalindrome(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i = 10**n-1
		while i >= 10**(n-1):
			number = str(i)+str(i)[::-1]
			

print(Solution().largestPalindrome(2))