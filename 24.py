#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		p = head
		head = head.next
		q = None
		while p!=None and p.next != None:
			if q != None:
				q.next.next = p.next
			q= p.next
			p.next = p.next.next
			q.next = p
			p = p.next
		return head
a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(2)
e = ListNode(4)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
solution = Solution()
result = solution.swapPairs(a)
while True:
	print(result.val)
	result = result.next
	if result == None:
		break