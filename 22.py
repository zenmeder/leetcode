#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def generateParenthesis(self, n):
		#这种做法时间复杂度很高，只能击败0.09%的人，太差
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n == 1:
			return ["()"]
		a = self.generateParenthesis(n-1)
		result = []
		for p in a:
			#取出a中的每一个元素
			for i in range(len(p)):
				tmp = p[:i]+'('+p[i:]
				for j in range(i+1,len(tmp)):
					t = tmp[:j]+')'+tmp[j:]
					if t not in result:
						result.append(t)
		return result
	def method1(self,n):
		if n == 1:
			return ["()"]
		a = self.method1(n-1)
		result = set()
		for p in a:
			result.add('()'+p)
			for i in range(len(p)):
				if p[i] == '(':
					result.add(p[:i+1]+'()'+p[i+1:])
		return result

solution = Solution()
print(solution.method1(4))