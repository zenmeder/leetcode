#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		intervals = sorted(intervals,key=lambda x:x.start)
		result = []
		for i in range(len(intervals)):
			if len(result) == 0:
				result.append(intervals[0])
				continue
			r = result[-1]
			if intervals[i].start > r.end:
				result.append(intervals[i])
				continue
			elif intervals[i].start <= r.end:
				result[-1] = Interval(r.start, max(r.end, intervals[i].end))
				continue

		return result

a = []
solution = Solution()
print(solution.merge(a))
for i in solution.merge(a):
	print(i.start,i.end)