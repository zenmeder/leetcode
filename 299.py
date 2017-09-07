#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def getHint(self, secret, guess):
		bull = cow = 0
		d = {}
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				bull += 1
			elif secret[i] in d:
				d[secret[i]] += 1
			else:
				d[secret[i]] = 1
		for i in range(len(guess)):
			if guess[i] in d and d[guess[i]] != 0 and guess[i] != secret[i]:
				cow += 1
				d[guess[i]] -= 1
		return "{bull}A{cow}B".format(bull = bull, cow = cow)
print(Solution().getHint('11','10'))