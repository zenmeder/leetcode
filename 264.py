#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import heapq

class Solution(object):
	def nthUglyNumber(self, n):
		res = [1]
		f2, f3, f5 = 0, 0, 0
		for i in range(1, n):
			res.append(min([res[f2]*2, res[f3]*3, res[f5]*5]))
			if res[-1] == res[f2]*2: f2+=1
			if res[-1] == res[f3]*3: f3+=1
			if res[-1] == res[f5]*5: f5+=1
		return res

print(Solution().nthUglyNumber(10))
