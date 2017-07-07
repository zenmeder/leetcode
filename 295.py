#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class MedianFinder(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.a = []

	def addNum(self, num):
		"""
		:type num: int
		:rtype: void
		"""
		self.a.append(num)
		self.a.sort()

	def findMedian(self):
		"""
		:rtype: float
		"""
		nums = self.a[:]
		if len(nums) == 1:
			return nums[0]
		elif len(nums)%2:

			return nums[int((len(nums)-1)/2)]
		else:
			return (nums[int(len(nums)/2)]+nums[int(len(nums)/2-1)])/2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
# param_2 = obj.findMedian()
obj.addNum(3)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())
obj.addNum()
print(obj.findMedian())
