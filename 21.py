#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		#假设从小到大排列
		# head = l1 if l1.val < l2.val else l2
		p = l1
		q = l2
		r = ListNode(0)
		s = r
		while p != None or q != None:
			if q== None:
				r.next = p
				p = p.next
			elif p == None:
				r.next = q
				q = q.next
			elif p.val < q.val:
				r.next = p
				p = p.next
			else:
				r.next = q
				q = q.next
			r = r.next
		return s.next
solution = Solution()
a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(2)
e = ListNode(4)
f = ListNode(6)
a.next = b
b.next = c
d.next = e
e.next = f
# print(solution.mergeTwoLists(a,d))
result = solution.mergeTwoLists(a,d)
while True:
	print(result.val)
	result = result.next
	if result == None:
		break