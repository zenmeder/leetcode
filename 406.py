#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def reconstgructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		res = []
		while people:
			tallest = sorted(self.getTallest(people), key=lambda x: x[1])
			if not res:
				res += tallest
			else:
				for p in tallest:
					res.insert(p[1], p)

		return res

	def getTallest(self, people):
		tallest = max([p[0] for p in people])
		res = [p for p in people if p[0]==tallest]
		for p in res:
			people.remove(p)
		return res



print(Solution().reconstgructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
