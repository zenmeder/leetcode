#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from functools import reduce

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if not head:
			return head
		nums = {}
		while head:
			if not nums or head.val not in nums:
				nums[head.val] = head
			elif head.val in nums:
				nums[head.val] = -1
			head = head.next
		nums = [i for i in sorted(nums.keys()) if nums[i] != -1]
		h = None
		for i in range(len(nums)):
			if not h:
				head = h = ListNode(nums[i])
			else:
				h.next = ListNode(nums[i])
				h = h.next
		return head
a = ListNode(2)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
r = Solution().deleteDuplicates(a)
while r:
	print(r.val)
	r = r.next