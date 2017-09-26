#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class NumMatrix(object):
	def __init__(self, matrix):
		"""
		:type matrix: List[List[int]]
		"""
		self.matrix = matrix
		self.cache = {}

	def sumRegion(self, row1, col1, row2, col2):
		"""
		:type row1: int
		:type col1: int
		:type row2: int
		:type col2: int
		:rtype: int
		"""
