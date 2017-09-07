#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	if version >=1:
		return True
	else:
		return False

class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i = 1
		j = n
		while i <= j:
			print(i,j)
			mid = (i+j)//2
			if j - i == 1 or i==j:
				return i if isBadVersion(i) else j
			if isBadVersion(mid):
				j = mid
				continue
			else:
				i = mid
				continue

print(Solution().firstBadVersion(1))