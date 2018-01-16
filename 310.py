#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i):
            for edge in edges:
                if edge[0] == i and edge[1] not in visited_edges:
                    visited_edges[edge[1]] = True
                    self.height += 1
                    dfs(edge[1])
                    self.height -= 1
                if edge[1] == i  and edge[0] not in visited_edges:
                    visited_edges[edge[0]] = True
                    self.height += 1
                    dfs(edge[0])
                    self.height -= 1
                self.maxHeight = max(self.maxHeight, self.height)
            return self.maxHeight
        maxHeight, res= 0, {}
        for edge in edges:
            if edge[0] not in res:
                visited_edges = {edge[0]:True}
                self.height, self.maxHeight = 0, 0
                res[edge[0]] = dfs(edge[0])
            if edge[1] not in res:
                visited_edges = {edge[1]:True}
                self.height, self.maxHeight = 0, 0
                res[edge[1]] = dfs(edge[1])
        a, b = [], float('inf')
        for (i,j) in res.items():
            if j < b:
                a, b= [i],j
            elif j == b:
                a.append(i)
        return a

# a = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
a = []
print(Solution().findMinHeightTrees(6, a))