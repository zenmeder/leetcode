#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def replaceWords(self, dict, sentence):
		"""
		:type dict: List[str]
		:type sentence: str
		:rtype: str
		"""
		sentence = sentence.split()
		for key, word in enumerate(sentence[:]):
			root = self.findShortestRoot(dict, word)
			if root:
				sentence[key] = root
		return ' '.join(sentence)

	def findShortestRoot(self, dict, word):
		short = None
		for root in dict:
			if word.startswith(root):
				if not short:
					short = root
				else:
					short = root if len(root) < len(short) else short
		return short

print(Solution().replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery"))
