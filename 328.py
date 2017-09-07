#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None or head.next == None or head.next.next == None:
			return head
		p = head
		q = head.next
		r = head.next.next
		while r:
			s = p.next
			p.next = r
			q.next = r.next
			r.next = s
			p = r
			q = q.next
			if not q:
				break
			r = q.next
		return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
result = Solution().oddEvenList(c)
while True:
	print(result.val)
	result = result.next
	if result == None:
		break
