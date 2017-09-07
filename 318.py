#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import time
class Solution(object):
	# def maxProduct(self, words):
	# 	"""
	# 	:type words: List[str]
	# 	:rtype: int
	# 	"""
	# 	words = sorted(words, key=lambda x: len(x), reverse=True)
	# 	maxProduct = 0
	# 	for i in range(len(words)-1):
	# 		for j in range(i+1, len(words)):
	# 			if len(words[i])*len(words[j]) < maxProduct:
	# 				break
	# 			if self.intersect(words[i],words[j]):
	# 				maxProduct = max(maxProduct, len(words[i])*len(words[j]))
	# 	return maxProduct
	# def intersect(self, s1, s2):
	# 	if not set(s1).intersection(set(s2)):
	# 		return True
	# 	return False
	def maxProduct(self, words):
		wordToNum = []
		for word in words:
			tmp = ['0']*26
			for letter in word:
				tmp[ord(letter)-ord('a')] = '1'
			wordToNum.append(int(''.join(tmp), 2))
		maxP = 0
		print(wordToNum)
		for i in range(len(words)-1):
			for j in range(i+1, len(words)):
				if not wordToNum[i] & wordToNum[j]:
					maxP = max(maxP, len(words[i])*len(words[j]))
		return maxP
t = time.time()
print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(time.time()-t)