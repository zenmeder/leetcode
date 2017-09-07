#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) < 2:
			return 0
		minPrice = None
		maxProfit = 0
		for price in prices:
			if minPrice == None or price < minPrice:
				minPrice = price
			else:
				maxProfit = max(maxProfit, price - minPrice)
		return maxProfit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
