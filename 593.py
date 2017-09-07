#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def validSquare(self, p1, p2, p3, p4):
		"""
		:type p1: List[int]
		:type p2: List[int]
		:type p3: List[int]
		:type p4: List[int]
		:rtype: bool
		"""
		nodes = [p1,p2,p3,p4]
		for node in nodes:
			r = []
			for n in nodes:
				if n != node:
					r.append(self.distance(node, n))
			r = sorted(r)
			if len(r)==3 and r[0] == r[1] and r[0]+r[1] == r[2]:
				continue
			else:
				return False
		return True
	def distance(self, n1, n2):
		return (n1[0]-n2[0])**2 + (n1[1]-n2[1])**2

print(Solution().validSquare([0,0],[0,0],[1,1],[0,0]))