#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		if not headA or not headB:
			return None
		a, b = [], []
		while headA:
			a.append(headA)
			headA = headA.next
		while headB:
			b.append(headB)
			headB = headB.next
		node = None
		while a and b:
			x , y = a.pop(), b.pop()
			if x == y:
				node = x
			else:
				break
		return node
