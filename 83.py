#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		p = head
		q = p.next
		while q:
			if q.val == p.val:
				p.next = q.next
			else:
				p = q
			q = p.next
		return head

a = ListNode(1)
b = ListNode(3)
c = ListNode(3)
d = ListNode(2)
e = ListNode(6)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
res = Solution().deleteDuplicates(a)
while res:
	print(res.val)
	res = res.next