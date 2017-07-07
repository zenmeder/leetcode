#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def reverseWords(self, s):
		p = 0
		str = ''
		while True:
			stack = []
			while p<len(s) and s[p] != ' ':
				stack.append(s[p])
				p+=1
			str+=''.join(stack[::-1])
			if p == len(s):
				break
			str+=' '
			p+=1
		return str

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest "))
