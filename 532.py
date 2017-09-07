#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import collections
class Solution(object):
	def findPairs(self, nums, k):
		if k > 0:
			return len(set(nums) & set(n + k for n in nums))
		elif k == 0:
			return sum(v > 1 for v in collections.Counter(nums).values())
		else:
			return 0

print(Solution().findPairs([1,3,1,5,4], 0))