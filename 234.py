#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length, p = 0, head
        while p:
            p, length = p.next, length + 1
        if length == 0 or length == 1:
            return True
        mid, i, q = (length + 1) // 2 if length % 2 else length // 2, 0, head
        while i < mid:
            q, i = q.next, i + 1
        r, s = q, q.next
        r.next = None
        while s:
            t = s.next
            s.next = r
            r, s = s, t
        while r and head:
            if r.val != head.val:
                return False
            r = r.next
            head = head.next
        return True

a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(1)
# a.next = b
# b.next = c
# c.next = d
print(Solution().isPalindrome(None))
