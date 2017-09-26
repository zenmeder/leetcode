#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        p = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        a = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0 or (matrix[i][j] >= matrix[i-1][j] and p[i-1][j]) or (matrix[i][j] >= matrix[i][j-1] and p[i][j-1]):
                    p[i][j] = True
        for i in range(len(matrix))[::-1]:
            for j in range(len(matrix[0]))[::-1]:
                if i==len(matrix)-1 or j==len(matrix[0])-1 or (matrix[i][j] >= matrix[i+1][j] and a[i+1][j]) or (matrix[i][j] >= matrix[i][j+1] and a[i][j+1]):
                    a[i][j] = True
        return [[i,j] for i in range(len(matrix)) for j in range(len(matrix[0])) if p[i][j] and a[i][j]]
# print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(Solution().pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]))