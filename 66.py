#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		flag = 1
		for i in range(len(digits))[::-1]:
			d = digits[i]
			digits[i] = (d+flag) % 10
			flag = (d+flag) // 10
		return digits if not flag else [1]+digits

print(Solution().plusOne([0]))
