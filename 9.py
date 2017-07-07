#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isPalindrome(self, x):
		#ratio: top 94.87%
		"""
		:type x: int
		:rtype: bool
		"""
		x = str(x)
		i = 0
		j = len(x)-1
		flag = True
		while(1):
			if (x[i] != x[j]):
				flag = False
				break
			if (i >= j):
				break
			i+=1
			j-=1
		return flag
solution = Solution()
print(solution.isPalindrome(123421))