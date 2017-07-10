#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MinStack(object):
	# 利用两个stack实现 一个存储所有值，一个存储遇见的最小值
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []
		self.minstack = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self.stack.append(x)
		if len(self.minstack) == 0 or x <= self.minstack[-1]:
			self.minstack.append(x)

	def pop(self):
		"""
		:rtype: void
		"""

		a = self.stack.pop(-1)
		if self.minstack[-1] == a:
			self.minstack.pop(-1)
		return a

	def top(self):
		"""
		:rtype: int
		"""
		return self.stack[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.minstack[-1]

	# Your MinStack object will be instantiated and called as such:


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
