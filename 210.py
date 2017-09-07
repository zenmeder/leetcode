#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		rank = [0] * numCourses

		for i in range(numCourses):
			if rank[prerequisites[i][0]] > rank[prerequisites[i][1]]:
				continue
			else:
				rank[prerequisites[i][0]] = rank[prerequisites[i][1]] + 1

		new_rank = [[i, rank[i]] for i in range(len(rank))]
		new_rank = sorted(new_rank, key=lambda x: x[1])
		return [l[0] for l in new_rank]

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2],[1,2]]))