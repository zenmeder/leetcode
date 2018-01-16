#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        startDict = {intervals[i].start : i for i in range(len(intervals))}
        sortIntervals = sorted(intervals, key = lambda x: x.start)

        def find(i):
            low, high = 0, len(sortIntervals)-1
            while low <= high:
                mid = (low + high) //2
                if sortIntervals[mid].start < i:
                    low = mid + 1
                elif sortIntervals[mid].start > i:
                    high = mid - 1
                else:
                    return startDict[sortIntervals[mid].start]
            return -1 if low == len(sortIntervals) else startDict[sortIntervals[low].start]
        return [find(interval.end) for interval in intervals]

i = [Interval(3,4),Interval(2,3),Interval(1,2)]
i = []
print(Solution().findRightInterval(i))