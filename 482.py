#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import deque


class Solution(object):
	def licenseKeyFormatting(self, S, K):
		"""
		:type S: str
		:type K: int
		:rtype: str
		"""
		queue = deque()
		for i in range(len(S))[::-1]:
			if S[i] == '-':
				continue
			if '0' <= S[i] <= '9':
				queue.append(S[i])
			else:
				tmp = S[i].upper()
				queue.append(tmp)
		res = ''
		while queue:
			for i in range(K):
				cha = queue.popleft()
				res += cha
				if not queue:
					break
			if queue:
				res += '-'
		return res[::-1]

print(Solution().licenseKeyFormatting('2-4A0r7-4k',3))

