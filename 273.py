#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num==0:
			return 'ZERO'

		a = ['HUNDRED','THOUSAND', 'MILLION', 'BILLION']
