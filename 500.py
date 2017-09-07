#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		row1 = {letter:1 for letter in ['Q','W','E','R','T','Y','U','I','O','P']}
		row2 = {letter:1 for letter in ['A','S','D','F','G','H','J','K','L']}
		row3 = {letter:1 for letter in ['Z','X','C','V','B','N','M']}
		res = []
		for word in words:
			word_upper = word.upper()
			flag = 0
			if word_upper[0] in row1:
				row = row1
			elif word_upper[0] in row2:
				row = row2
			elif word_upper[0] in row3:
				row = row3
			for i in range(1,len(word_upper)):
				if word_upper[i] not in row:
					flag = 1
					break
			if not flag:
				res.append(word)
		return res

print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))