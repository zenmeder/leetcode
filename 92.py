#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		if not head:
			return head
		p = head
		for i in range(m - 2):
			p = p.next
		node1 = p
		flag = 0
		if m!=1:
			p = p.next
			flag = 1
		node2 = p
		q = p.next
		p.next = None
		i = 0
		while q and i < n - m:
			r = q.next
			q.next = p
			p = q
			q = r
			i += 1
		node3 = p
		node4 = q
		node1.next = node3
		node2.next = node4
		return head if flag else p

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
res = Solution().reverseBetween(a,4,5)
while res:
	print(res.val)
	res = res.next