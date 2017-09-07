#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		p = head
		q = head.next
		head.next = None
		while p:
			r = q.next
			q.next = p
			p = q
			q = r
		return p