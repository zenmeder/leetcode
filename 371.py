#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def getSum(self, a: int, b: int) -> int:
		# todo: 只支持非负数的相加，负数不支持
		a, b = bin(a)[2:][::-1], bin(b)[2:][::-1]
		la, lb = len(str(a)), len(str(b))
		if la > lb:
			b += '0' * (la - lb)
		else:
			a += '0' * (lb - la)
		res = []
		y = 0
		for i in range(max(la,lb)):
			x = int(a[i]) ^ int(b[i]) ^ y
			y = (int(a[i]) & int(b[i])) | ((int(a[i]) ^ int(b[i])) & y)
			res.append(str(x))
		if y:
			res.append(str(y))
		return int(''.join(res[::-1]), base=2)


print(Solution().getSum(-1,1))
