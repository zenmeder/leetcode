#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""

		p = head
		if not p:
			return p
		small = big = None
		small_start = big_start = None
		while p:
			if small == None and p.val < x:
				small = p
				small_start = small
			elif big == None and p.val >= x:
				big = p
				big_start = big
			elif p.val < x:
				small.next = p
				small = p
			elif p.val >= x:
				big.next = p
				big = p
			p = p.next
		if small:
			small.next = None
		if big:
			big.next = None
		if small_start:
			small.next = big_start
			return small_start
		else:
			return big_start
a = ListNode(2)
b = ListNode(1)
c = ListNode(5)
d = ListNode(2)
e = ListNode(4)
f = ListNode(6)
a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
result = Solution().partition(a,0)
while result:
	print(result.val)
	result = result.next

