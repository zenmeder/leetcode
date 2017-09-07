#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		"""
		:type timeSeries: List[int]
		:type duration: int
		:rtype: int
		"""
		if not timeSeries:
			return 0
		l = []
		for time in timeSeries:
			if not l:
				l = [time, time + duration]
				res = duration
				continue
			if time >= l[1]:
				l = [time, time + duration]
				res += duration
			else:
				res += time + duration - l[1]
				l[1] = time + duration
		return res


print(Solution().findPoisonedDuration([1, 2, 3, 4, 5], 5))
