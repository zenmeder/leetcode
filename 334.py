#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def increasingTriplet(self, nums):
		first = second = float('inf')
		for n in nums:
			if n <= first:
				first = n
			elif n <= second:
				second = n
			else:
				return True
		return False



print(Solution().increasingTriplet([2,1,5,2,3]))
