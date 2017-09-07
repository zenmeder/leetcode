#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isPerfectSquare(self, num):
		if num == 1:
			return True
		i = 1
		j = num - 1
		while i <= j:
			mid = (i + j) // 2
			if mid ** 2 == num:
				return True
			elif mid ** 2 > num:
				j = mid - 1
				continue
			elif mid ** 2 < num:
				i = mid + 1
				continue
		return False

print(Solution().isPerfectSquare(1024))
