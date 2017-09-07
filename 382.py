#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import random
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		:type head: ListNode
		"""
		self.nums = []
		while head:
			self.nums.append(head.val)
			head = head.next

	def getRandom(self):
		"""
		Returns a random node's value.
		:rtype: int
		"""
		return random.choice(self.nums)

a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(2)

print(Solution(a).getRandom())