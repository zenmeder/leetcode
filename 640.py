#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def solveEquation(self, equation):
		s1 = 0
		s2 = 0
		flag = 1
		i = 0
		num = [str(i) for i in range(10)]
		while i < len(equation):
			if equation[i] == '=':
				flag = -1
				i += 1
			elif equation[i] == '+' or equation[i] == '-' or equation[i] in num:
				tmp = equation[i]
				i += 1
				while i < len(equation) and equation[i] in num:
					tmp += equation[i]
					i += 1
				if i < len(equation):
					if equation[i] == 'x':
						if i == 0 or equation[i - 1] == "+" or equation[i - 1] == "-" or equation[i - 1] == "=":
							tmp += '1'
						s1 += int(tmp) * flag
						i += 1
					else:
						s2 += int(tmp) * flag
				else:
					s2 += int(tmp) * flag
			elif equation[i] == 'x':
				s1 += flag
				i += 1
		if s1 == 0 and s2 != 0:
			return 'No solution'
		elif s1 == 0 and s2 == 0:
			return 'Infinite solutions'
		else:
			return "x={}".format(int(-s2 / s1))


solution = Solution()
print(solution.solveEquation('2x=x'))
