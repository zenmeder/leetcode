#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		while head and head.val == val:
			head = head.next
		p = head
		if not head or not head.next:
			return p
		q = head.next
		while q:
			if q.val == val:
				q = q.next
			else:
				p.next = q
				p = q
				q = q.next
		p.next = None
		return head

a = ListNode(4)
b = ListNode(4)
c = ListNode(4)
d = ListNode(4)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
r = Solution().removeElements(a,4)
while r:
	print(r.val)
	r = r.next

