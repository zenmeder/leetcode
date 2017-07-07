#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def son(self, y):
		self.next = y

class Solution():
	def addTwoNumbers(self, l1, l2):
		flag = 0
		if l1.val + l2.val < 10:
			l3 = ListNode(l1.val + l2.val)
		else:
			l3 = ListNode(l1.val + l2.val - 10)
			flag = 1
		head = l3
		while l1.next and l2.next:
			l3.next = ListNode((l1.next.val + l2.next.val + flag) % 10)
			flag = (l1.next.val + l2.next.val + flag) / 10
			l1 = l1.next
			l2 = l2.next
			l3 = l3.next
		if l1.next:
			while l1.next:
				l3.next = ListNode((l1.next.val + flag) % 10)
				flag = (l1.next.val + flag) / 10
				l1 = l1.next
				l3 = l3.next
		if l2.next:
			while l2.next:
				l3.next = ListNode((l2.next.val + flag) % 10)
				flag = (l2.next.val + flag) / 10
				l2 = l2.next
				l3 = l3.next
		if flag:
			l3.next = ListNode(1)
		return head

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.son(l2)
l2.son(l3)

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.son(l5)
l5.son(l6)

# print(l1.next.next.val, l4.next.next.val)
# l3 = l1.next
# print(l3)
solution = Solution()
l = solution.addTwoNumbers(l1, l4)
print(l.next.next.val)
