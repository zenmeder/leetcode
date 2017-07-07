#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		length = len(height)
		a = []
		p = 0
		result = 0
		while p <= length - 3:
			if height[p] == 0:
				continue
			start = p
			while height[p+1]<= height[start]:
				p+=1
			stop = p
			for i in range()

solution = Solution()
print(solution.trap([5, 2, 1, 2, 1, 5]))
