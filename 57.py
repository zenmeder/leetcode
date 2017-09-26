#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        length = len(intervals)
        i, j = 0, length - 1
        while i <= j:
            mid = (i + j) // 2
            if intervals[mid].start < newInterval.start:
                i = mid + 1
            else:
                j = mid - 1
        if i:
            if intervals[i - 1].start <= newInterval.start <= intervals[i - 1].end:
                intervals[i - 1].end = max(newInterval.end, intervals[i - 1].end)
                res = intervals[:i]
            else:
                res = intervals[:i]+[newInterval]
        else:
            res = [newInterval]

        while i < length:
            if res[-1].start <= intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res += intervals[i:]
                break
            i += 1
        print([[a.start, a.end] for a in res])
        return res
a = Interval(1, 2)
b = Interval(3, 5)
# Solution().insert([a],b)
c = Interval(6, 7)
d = Interval(8, 10)
e = Interval(12, 16)
f = Interval(1,1)
Solution().insert([a, b, c, d, e], f)
