#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		a = []
		for i in range(len(s)):
			print(s[i])
			if s[i] in ['(', '{', '[']:
				a.append(s[i])
			else:
				if len(a) == 0:
					return False
				# if ord(s[i]) == ord(a[-1]) + 1 or ord(s[i]) == ord(a[-1]) + 2:
				if (s[i] == ')' and a[-1] == '(') or (s[i] == ']' and a[-1] == '[') or (s[i] == '}' and a[-1] == '{'):
					a.pop(-1)
				else:
					return False
		return True if len(a)==0 else False

solution = Solution()
print(solution.isValid('(]'))