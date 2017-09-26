#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		dps = []
		di = {word:i for i, word in enumerate(wordDict)}
		for i in range(len(s)):
			if i == 0:
				dps.append([[di[s[0]]]]) if s[0] in di else dps.append([])
				continue
			tdp = []
			if s[:i+1] in di:
				tdp.append([di[s[:i+1]]])
			for j in range(i):
				if dps[j] and s[j+1:i+1] in di:
					for dp in dps[j]:
						tdp.append(dp+[di[s[j+1:i+1]]])
			dps.append(tdp)
		sentences = []
		for dp in dps[-1]:
			sentences.append(' '.join([wordDict[i] for i in dp]))

		return sentences

# print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
