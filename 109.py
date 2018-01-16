#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def listToBST(l):
            length = len(l)
            if length == 1:
                return TreeNode(l[0])
            elif length == 0:
                return None
            mid = length//2
            p = TreeNode(l[mid])
            p.left = listToBST(l[:mid])
            p.right = listToBST(l[mid+1:])
            return p

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return listToBST(nums)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

h = Solution().sortedListToBST(a)
print(h.val)
print(h.left.val)
print(h.right.val)
print(h.right.left.val)

