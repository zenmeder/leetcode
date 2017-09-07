#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num == 0:
			return False
		while not num % 5:
			num /= 5
		while not num % 3:
			num /= 3
		while not num % 2:
			num /= 2
		if num == 1:
			return True
		return False


