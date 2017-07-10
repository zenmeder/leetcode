#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if head==None:
			return head
		p = head
		length = 1
		while p.next != None:
			p = p.next
			length += 1
		p.next = head
		p = head
		k %= length
		if k != length:
			for i in range(length - k - 1):
				p = p.next
			result = p.next
			p.next = None
			return result
		elif k == length:
			return head



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
r = Solution().rotateRight(a, 4)
while r.next != None:
	print(r.val)
	r = r.next
print(r.val)
