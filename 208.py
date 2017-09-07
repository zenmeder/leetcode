#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Trie(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = dict()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		# for i, letter in enumerate(word):
		# 	if letter not in self.root:
		# 		break
		# for letter in word[i:]:
		# 	self.root
		root = self.root
		for i, letter in enumerate(word):
			if letter not in root :
				root.setdefault(letter, {})
			if i == len(word) - 1:
				root[letter]['Z'] = 1
			root = root[letter]
	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		root = self.root
		for letter in word:
			if letter not in root:
				return False
			root = root[letter]
		if 'Z' in root:
			return True
		return False

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		root = self.root
		for letter in prefix:
			if letter not in root:
				return False
			root = root[letter]
		return True

a = Trie()
# a.insert('abd')
# a.insert('abcd')
a.insert('ab')
print(a.search('ab'))
print(a.startsWith('a'))