#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def removeNthFromEnd(self, head, n):
		# 拿数组存储
		nodeList = []
		p = head
		while p.next != None:
			nodeList.append(p)
			p = p.next
		pos = len(nodeList) - n + 1
		if pos == 0:
			return head.next
		elif pos == len(nodeList):
			nodeList[-n].next = None
		else:
			nodeList[-n].next = nodeList[-n + 1].next
		return head

	def method2(self, head, n):
		# 两个指针，一个比另一个走快n步
		p = q = head
		for i in range(n):
			q = q.next
		if q == None:
			return head.next
		while q.next != None:
			p = p.next
			q = q.next
		p.next = p.next.next
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
head = Solution().method2(a, 3)
while head.next != None:
	print(head.val)
	head = head.next
print(head.val)
