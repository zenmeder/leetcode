#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math
class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		if amount == 0:
			return 0
		coins, combs = sorted(coins), [1] + [float('inf')] * amount
		for i in range(amount + 1):
			for coin in coins:
				if coin > i: break
				if coin == i: combs[i] = 1
				if coin < i: combs[i] = min(combs[i],combs[i-coin]+1)
		return combs[amount] if not math.isinf(combs[amount]) else -1
print(Solution().coinChange([2],1))

