#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import heapq

class Solution(object):
	def nthUglyNumber(self, n):
		uglies = [1]
		def gen(param):
			for ugly in uglies:
				yield ugly * param

		merged = heapq.merge(*map(gen, [2,3,5]))
		while len(uglies) < n:
			ugly = next(merged)
			if ugly != uglies[-1]:
				uglies.append(ugly)

		return uglies[-1]


print(Solution().nthUglyNumber(10))
