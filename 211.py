#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class WordDictionary(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.wd = dict()

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: void
		"""
		wd = self.wd
		for i, letter in enumerate(word):
			if letter not in wd:
				wd.setdefault(letter, {})
			if i == len(word)-1:
				wd[letter]['Z'] = 1
			wd = wd[letter]
	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		wd = self.wd
		d = [wd]
		for letter in word:
			nd = []
			for w in d:
				if type(w) != dict:
					continue
				if letter in w:
					nd.append(w[letter])
				if letter == '.':
					for a in w:
						nd.append(w[a])
			d = nd[:]
		for di in d:
			if type(di)==dict and 'Z' in di:
				return True
		return False

a = WordDictionary()
a.addWord('ran')
a.addWord('rune')
a.addWord('runner')
a.addWord('runs')
a.addWord('add')
a.addWord('adds')
a.addWord('adder')
a.addWord('addee')
# print(a.search('r.n'))
# print(a.search('ru.n.e'))
# print(a.search('add'))
# print(a.search('add.'))
# print(a.search('adde.'))
# print(a.search('.an.'))
# print(a.search('...s'))
print(a.search('..n.r'))
# print(a.search('.'))
# print(a.search('a'))
# print(a.search('aa'))
# print(a.search('a'))
# print(a.search('.a'))