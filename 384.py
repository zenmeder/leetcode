#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from itertools import permutations
import random

class Solution(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.n = nums
		self.length = len(nums)
	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self.n

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		nums = self.n[:] #type: list
		result = []
		for i in range(self.length):
			r = random.randrange(0, len(nums))
			result.append(nums[r])
			del nums[r]
		return result

a = Solution([])
print(a.shuffle())
print(a.reset())
