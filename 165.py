#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def compareVersion(self, version1, version2):
		a = version1.split('.')
		b = version2.split('.')
		i = 0
		while i < len(a) and i < len(b):
			if a[i] < b[i]:
				return -1
			elif a[i] > b[i]:
				return 1
			else:
				i += 1
		return 0


solution = Solution()
print(solution.compareVersion('1.2.3', '1.2.3'))
