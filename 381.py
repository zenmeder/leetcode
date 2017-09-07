#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import random
class RandomizedCollection(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.l = []
	def insert(self, val):
		"""
		Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		l = self.l
		flag = True if val in l else False
		l.append(val)
		return flag
	def remove(self, val):
		"""
		Removes a value from the collection. Returns true if the collection contained the specified element.
		:type val: int
		:rtype: bool
		"""
		l = self.l
		if val in l:
			l.remove(val)
			return True
		return False

	def getRandom(self):
		"""
		Get a random element from the collection.
		:rtype: int
		"""
		l = self.l
		return l[random.randrange(0, len(l))]


		# Your RandomizedCollection object will be instantiated and called as such:
		# obj = RandomizedCollection()
		# param_1 = obj.insert(val)
		# param_2 = obj.remove(val)
		# param_3 = obj.getRandom()