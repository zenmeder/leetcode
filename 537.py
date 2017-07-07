#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def complexNumberMultiply(self, a, b):
		a = a.split("+")
		b = b.split("+")
		a_real = int(a[0])
		a_complex = int(a[1][:-1])
		b_real = int(b[0])
		b_complex = int(b[1][:-1])
		real = a_real*b_real-a_complex*b_complex
		complex = a_real*b_complex+a_complex*b_real
		return '{0}+{1}i'.format(real,complex)

solution = Solution()
print(solution.complexNumberMultiply("1+-1i", "1+-1i"))
