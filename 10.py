#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if p == '' and s == '':
			return True
		if len(s) == 1 and len(p) == 1 and (s == p or p == '.'):
			return True
		if p[1] != '*' :
			if len(s) == 0:
				return False
			elif s[0] == p[0]:
				s = s.replace(s[0],'',1)
				p = p.replace(p[0],'',1)
				return self.isMatch(s,p)
		if p[1] == '*':
			if len(s)!=0  and s[0] == p[0]:
				p = p.replace(p[0],'',1)
				p = p.replace(p[0],'',1)
				if self.isMatch(s,p):
					return True
				else:
					s = s.replace(s[0],'',1)
					return self.isMatch(s,p)

solution = Solution()
print(solution.isMatch('abc','ab*'))
