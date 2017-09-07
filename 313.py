#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

import heapq
class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		uglies = [1]

		def gen(prime):
			for ugly in uglies:
				yield ugly * prime

		merged = heapq.merge(*map(gen, primes))
		while len(uglies) < n:
			ugly = next(merged)
			if ugly != uglies[-1]:
				uglies.append(ugly)
		return uglies[-1]

print(Solution().nthSuperUglyNumber(10,[2, 7, 13, 19]))