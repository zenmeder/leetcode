#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from functools import reduce

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if not head or not head.next:
			return head
		target = head.val
		p = head.next
		if p.val != target:
			head.next = self.deleteDuplicates(p)
			return head
		else:
			while p and p.val == target:
				p = p.next
			return self.deleteDuplicates(p)
a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(5)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
r = Solution().deleteDuplicates(a)
while r:
	print(r.val)
	r = r.next