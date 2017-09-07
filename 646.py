#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findLongestChain(self, pairs):
		"""
		:type pairs: List[List[int]]
		:rtype: int
		"""
		pairs.sort()
		d = {}
		a = []
		for pair in pairs:
			if pair[0] in d:
				continue
			a.append(pair)
		b = a[:]
		for i in range(len(b)):
			if i >= len(b)-1:
				break
			print(b,i)
			if b[i][1] == b[i+1][0] or  (b[i+1][1] >b[i][1] > b[i+1][0]):
				del(b[i+1])
			elif b[i][1] > b[i+1][1]:
				del(b[i])
		return len(b)


print(Solution().findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]))
