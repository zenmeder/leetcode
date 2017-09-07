#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from math import sqrt,floor
class Solution(object):
	def bulbSwitch(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return int(floor(sqrt(n)))
