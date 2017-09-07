#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		i = 0
		stack = []
		while i < len(s):
			if '0' <= s[i] <= '9' or 'a' <= s[i] <= 'z' or s[i] == '[':
				stack.append(s[i])
			elif s[i] == ']':
				pop = stack.pop()
				tmp = []
				while pop != '[' and len(stack) > 0:
					tmp.append(pop)
					pop = stack.pop()
				pop = stack.pop()
				num = ''
				flag = 0
				while '0' <= pop <= '9':
					num += pop
					if len(stack)>0:
						pop = stack.pop()
					else:
						flag = 1
						break
				if not flag:
					stack.append(pop)
				stack.append(''.join(tmp[::-1])*int(num[::-1]))
			i += 1
		return stack

print(Solution().decodeString("2[ab3[cd]]4[xy]"))
