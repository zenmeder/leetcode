#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == head:
            return head
        slow = fast = head
        meet = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = True
                break
        if not meet:
            return None
        start1, start2 = head, slow
        while start1 != start2:
            start1 = start1.next
            start2 = start2.next
        return start1.val

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = a
# b.next = c
# c.next = d
# d.next = a
print(Solution().detectCycle(a))


