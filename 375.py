#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		low = 1
		high = n
		money = 0
		while low <= high:
			mid = (low + high) // 2
			if guess(mid) == 0:
				break
			elif guess(mid) == -1:
				money += mid
				high = mid - 1
			elif guess(mid) == 1:
				money += mid
				low = mid + 1
		return money
