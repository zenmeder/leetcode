#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		head = ListNode(0)
		p = []
		q = []
		for i in range(len(lists)):
			p[i] = lists[i]
			q[i] = p[i].val
		while True:

	# def findSmallest(self, p):
