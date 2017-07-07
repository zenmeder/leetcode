#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import string


class Solution(object):
	def reverse(self, x):
		# ratio: top 64.37%
		if(x == 0):
			return 0
		x = str(x)
		if x[0] == '-':
			a = '-' + x[1::][::-1]
		else:
			a = x[::-1]
		i = 0
		while (1):
			if (a[i] == '-'):
				i += 1
				continue
			elif (a[i] == '0'):
				i += 1
				a = a.replace(a[i], '', 1) # replace返回的才是替换过的字符串 此处不可以是 a.replace(a[i], '', 1)
				continue
			break
		a = int(a)
		if 2147483647 < a or a < -2147483648:
			return 0
		return a


solution = Solution()
print(solution.reverse(0))
