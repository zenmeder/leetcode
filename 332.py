#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		for i in range(len(tickets)):
			if tickets[i][0] == 'JFK':
