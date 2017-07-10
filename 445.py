#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# print(self.lnToNum(l1))
		return self.numToLn(self.lnToNum(l1)+self.lnToNum(l2))
	def lnToNum(self, l):
		num = 0
		while l != None:
			num = 10 * num + l.val
			l = l.next
		return num
	def numToLn(self, num):
		head = None
		nums = str(num)
		for i in range(len(nums)):
			if head==None:
				head = ListNode(int(nums[i]))
				p = head
			else:
				p.next = ListNode(int(nums[i]))
				p = p.next
		return head
solution = Solution()
# print()
a = solution.numToLn(3427)
b = solution.numToLn(465)
print(solution.lnToNum(solution.addTwoNumbers(a,b)))