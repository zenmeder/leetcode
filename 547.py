#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            color[i][j] = 1
            color[j][i] = 1
            for k in range(len(M)):
                if not color[k][j] and M[k][j]:
                    dfs(k,j)
            for k in range(len(M[0])):
                if not color[i][k] and M[i][k]:
                    dfs(i,k)

        if not M or not M[0]:
            return 0
        color = [[0]*len(M[0]) for _ in range(len(M))]
        res = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] and not color[i][j]:
                    res += 1
                    dfs(i, j)
        return res

g = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print(Solution().findCircleNum(g))