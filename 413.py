#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def numberOfArithmeticSlices(self, A):
		length = len(A)
		if length <= 2:
			return 0
		i = 0
		count = 0
		while i < length - 2:
			j = i + 2
			while j < length:
				if self.judge(A, i, j):
					count += 1
					j += 1
				else:
					break
			i += 1
		return count

	def judge(self, A, start, stop):
		flag = 1
		for i in range(start, stop + 1):
			if A[i] != A[start]+(i-start)*(A[start+1]-A[start]):
				flag = 0

		return flag

solution = Solution()
print(solution.numberOfArithmeticSlices([1,2,3,4,5,6]))
# print(solution.judge([1,2,3,8,9,10],0,2))
