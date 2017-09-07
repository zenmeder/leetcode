#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return None
		values = []
		while head:
			values.append(head.val)
			head = head.next
		values = sorted(values)
		head = ListNode(values[0])
		copy = head
		for i in range(1, len(values)):
			copy.next = ListNode(values[i])
			copy = copy.next
		return head

a = ListNode(3)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
res = Solution().sortList(None)
while res:
	print(res.val)
	res = res.next

