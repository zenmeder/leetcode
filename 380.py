#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from random import random,randint

class RandomizedSet(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.s = set()

	def insert(self, val):
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		:type val: int
		:rtype: bool
		"""
		s = self.s
		if s.__contains__(val):
			return False
		else:
			s.add(val)
			return True
	def remove(self, val):
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		:type val: int
		:rtype: bool
		"""
		s = self.s
		if s.__contains__(val):
			s.remove(val)
			return True
		else:
			return False

	def getRandom(self):
		"""
		Get a random element from the set.
		:rtype: int
		"""
		return list(self.s)[randint(0, len(self.s)-1)]

