#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findMinDifference(self, timePoints):
		"""
		:type timePoints: List[str]
		:rtype: int
		"""

		timePoints.sort()
		minMinute = None
		for i in range(1, len(timePoints)):
			if minMinute == None:
				minMinute = self.timeMinus(timePoints[i], timePoints[i - 1])
			else:
				minMinute = min(minMinute, self.timeMinus(timePoints[i], timePoints[i - 1]))
		if self.timeMinus(timePoints[0], timePoints[-1]) > 0:
			return min(minMinute,self.timeMinus(timePoints[0], timePoints[-1]))
		else:
			return minMinute

	def timeMinus(self, time1, time2):
		# time1>time2
		l1 = time1.split(":")
		l2 = time2.split(":")
		if int(l1[0]) - int(l2[0]) >= 0:
			return (int(l1[0]) - int(l2[0])) * 60 + (int(l1[1]) - int(l2[1]))
		else:
			return (int(l1[0]) - int(l2[0]) + 24) * 60 + (int(l1[1]) - int(l2[1]))

print(Solution().findMinDifference(["12:12","12:13"]))