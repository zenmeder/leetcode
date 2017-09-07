#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if not nums:
			return False
		d = dict()
		for num in nums:
			if num in d:
				return True
			d[num] = 1
		return False