#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		path = path.split('/')
		for dir in path[::-1]:
			if len(dir)!=0 and dir != '.':
				return '/{}'.format(dir)
		return '/'
print(Solution().simplifyPath('/..'))