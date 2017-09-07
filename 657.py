#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def judgeCircle(self, moves):
		"""
		:type moves: str
		:rtype: bool
		"""
		x, y = 0, 0
		for move in moves:
			if move == 'U':
				y += 1
			elif move == 'D':
				y -= 1
			elif move == 'R':
				x += 1
			elif move == 'L':
				x -= 1
		return x == 0 and y == 0
