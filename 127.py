#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		if endWord not in wordList:
			return 0
		words = {endWord: 1}

		while True:
			c = words.copy()
			for word in words.keys():
				for mword in wordList:
					if self.isOneLetterDiff(word, mword):
						if mword not in c:
							c[mword] = c[word] + 1
						else:
							c[mword] = min(c[word] + 1, c[mword])
			if words == c:
				break
			words = c.copy()

		res = float('inf')
		for word in words.keys():
			if self.isOneLetterDiff(word, beginWord):
				res = min(res, words[word]+1)
		return res

	def isOneLetterDiff(self, word1, word2):
		count = 0
		for i in range(len(word1)):
			if word1[i] != word2[i]:
				count += 1
			if count > 1:
				return False
		return True

print(Solution().ladderLength('hot','dog',["hot","dot","dog","lot","log","cog"]))