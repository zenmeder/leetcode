#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxProfit(self, prices):
		profit, i = [], 0
		while i < len(prices) - 1:
			j = i
			while j < len(prices) - 1 and prices[j] < prices[j + 1]:
				j += 1
			profit.append(prices[j] - prices[i])
			i = j + 1
		return sum(sorted(profit)[-2:])


print(Solution().maxProfit([4, 7, 1, 5, 3, 6, 4, 7, 10]))
