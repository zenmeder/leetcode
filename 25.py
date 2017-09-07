#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if head == None or head.next == None:
			return head
		p = q = head
		s = res = None
		while True:
			if p == None:
				break
			for i in range(k - 1):
				if q.next == None:
					if i != k - 1 and s == None:
						return p
					elif i != k - 1 and s != None:
						s.next = p
						return res
					break
				q = q.next
			if res == None:
				res = q
			r = q.next
			self.reverse(p, q)
			if s != None:
				s.next = q
				s = p
			else:
				s = p
			p = q = r
		return res

	def reverse(self, head, tail):
		# 将head和tail之间的链表反转，包括head和tail
		# 返回链表的头
		p = head
		q = head.next
		p.next = None
		while p != tail:
			r = q.next
			q.next = p
			p = q
			q = r
		return p


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
# head = Solution().reverse(b, d)
head = Solution().reverseKGroup(a, 3)
while head.next != None:
	print(head.val)
	head = head.next
print(head.val)
