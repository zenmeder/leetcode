#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def twoSum(self, numbers, target):
		i = 0
		j = len(numbers) - 1
		while i < j:
			if numbers[i] + numbers[j] == target:
				return [i, j]
			elif numbers[i] + numbers[j] < target:
				i += 1
			elif numbers[i] + numbers[j] > target:
				j -= 1
