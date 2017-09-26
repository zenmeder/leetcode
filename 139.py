#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	# dp
	def wordBreak(self, s, wordDict):
		if not s:
			return True
		if not wordDict:
			return False
		length = len(s)
		dps = ([True] if s[0] in wordDict else [False]) + [False]*(length-1)
		for i in range(1, length):
			if s[:i + 1] in wordDict:
				dps[i] = True
				continue
			for j in range(i):
				if dps[j] and s[j+1:i+1] in wordDict:
					dps[i] = True
					break
		return dps[-1]
	#recursive tle
	def wordBreak1(self, s, wordDict):
		wordDict = sorted(wordDict, key=lambda x: len(x), reverse=True)

		def wb(st, w):
			if not st:
				return True
			if not w or len(w) == 0:
				return False
			elif len(w) == 1:
				return st == w[0]

			for word in w:
				if st.startswith(word) and self.wordBreak(s[len(word):], w):
					return True
			return False

		return wb(s, wordDict)
print(Solution().wordBreak("leetcode"
,["leet","code"]))
# print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# ,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
