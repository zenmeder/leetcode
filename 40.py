#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		length = len(candidates)
		if length == 0 or (length == 1 and candidates[0] != target):
			return []
		return self.removeDup(self.recursion(candidates, length-1, target))

	def recursion(self, candidates, end, target):
		result = []
		if target==0:
			return [[]]

		if end == -1 or (end==0 and candidates[0] != target):
			return []
		if end == 0 and candidates[0] == target:
			return [[candidates[0]]]
		a = self.recursion(candidates, end - 1, target)
		for element in a:
			result.append(element)
		if candidates[end] <= target:
			b = self.recursion(candidates, end - 1, target - candidates[end])
			for element in b:
				result.append(element + [candidates[end]])
		return result
	def removeDup(self, l):
		s = set()
		result = []
		for subl in l:
			subl.sort()
			s.add(tuple(subl))
		for subs in s:
			result.append(list(subs))
		return result
solution = Solution()
print(solution.combinationSum2([0,0],0))