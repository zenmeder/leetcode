#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0:
			return ""
		if len(strs) == 1:
			return strs[0]
		minStr = 0
		for i in range(len(strs)):
			if len(strs[i]) < len(strs[minStr]):
				minStr = i

		maxLength = len(strs[minStr])
		for i in range(len(strs)):
			if i == minStr:
				continue
			j = 0
			while j< maxLength:
				if j == len(strs[minStr] or j == len(strs[i])) or strs[minStr][j]!=strs[i][j]:
					maxLength = min(maxLength,j)
				j+=1
		return strs[minStr][:maxLength]


solution = Solution()
print(solution.longestCommonPrefix(['c','a','c']))
