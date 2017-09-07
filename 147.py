#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

import bisect


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return head
		nodes = [head]
		nodesValue = [head.val]
		while head.next:
			head = head.next
			pos = bisect.bisect_left(nodesValue, head.val)
			nodes.insert(pos, head)
			nodesValue.insert(pos, head.val)
		for i in range(len(nodes)-1):
			nodes[i].next = nodes[i+1]
		nodes[-1].next = None
		return nodes[0]

a = ListNode(10)
a1 = ListNode(8)
a2 = ListNode(9)
a3 = ListNode(7)
# a.next = a1
# a1.next = a2
# a2.next = a3

c = Solution().insertionSortList(a)
while c:
	print(c.val)
	c = c.next
