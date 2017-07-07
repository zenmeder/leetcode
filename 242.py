#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		# ratio: 0.5%
		if len(s)!= len(t):
			return False
		for i in range(len(s)):
			if s[i] in t:
				t = t.replace(s[i], '', 1)
			else:
				return False
		return True

	def isAnagram1(self, s, t):
		# much better than above
		# ratio: 82.4%
		if len(s)!=len(t):
			return False
		a = [0 for i in range(26)]
		for i in range(len(s)):
			a[ord(s[i])-97]+=1
		for i in range(len(t)):
			a[ord(t[i])-97]-=1
		for i in range(26):
			if a[i]!=0:
				return False
		return True



solution = Solution()
# print(solution.isAnagram('abc', 'caba'))
print(solution.isAnagram1('abc','abcc'))