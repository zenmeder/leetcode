#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root):
    stack, res = [root], []
    visited = {}
    while stack:
        if stack[-1].left and stack[-1] not in visited:
            visited[stack[-1]] = 1
            stack.append(stack[-1].left)
        else:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
    return res


def preorder(root):
    stack, res = [root], []
    visited = {}
    while stack:
        if stack[-1] not in visited:
            res.append(stack[-1].val)
        if stack[-1].left and stack[-1] not in visited:
            visited[stack[-1]] = 1
            stack.append(stack[-1].left)
        else:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
    return res


def postorder(root):
    stack, res = [root], []
    visited = {}
    while stack:
        if stack[-1].left and stack[-1] not in visited:
            visited[stack[-1]] = 1
            stack.append(stack[-1].left)
        elif stack[-1].right and (stack[-1] not in visited or visited[stack[-1]] != 2):
            visited[stack[-1]] = 2
            stack.append(stack[-1].right)
        else:
            res.append(stack[-1].val)
            stack.pop()
    return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
# a.right = c
b.left = d
b.right = e

print(inorder(a))
print(preorder(a))
print(postorder(a))
