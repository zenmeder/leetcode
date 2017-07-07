#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def combinationSum(self, candidates, target):
		length = len(candidates)
		result = []
		if length==0:
			return []
		if length==1:
			if target%candidates[0]:
				return []
			else:
				result.append([candidates[0] for i in range(int(target/candidates[0]))])

		a = self.recurison(candidates,length-1,target)
		b = set()
		c = list()
		for element in a:
			b.add(tuple(element))
		for element in b:
			c.append(list(element))
		return c
	def recurison(self,candidates,end,target):
		result = []
		if end == -1:
			return []
		if end == 0:
			if target%candidates[0]:
				return []
			else:
				result.append([candidates[0] for i in range(int(target/candidates[0]))])
				return result
		if candidates[end] > target:
			return self.recurison(candidates,end-1,target)
		for i in range(int(target/candidates[end])+1):
			a = self.recurison(candidates,end-1,target-(i)*candidates[end])
			if i == 0:
				result+=a
			else:
				for element in a:
					result.append(element + [candidates[end] for j in range(i)])

		return result
solution = Solution()
print(solution.combinationSum([1,1,1,1],11))