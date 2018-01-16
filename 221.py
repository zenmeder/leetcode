#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.h = 0
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        def maxS(i, j, height):
            for di in range(height+1):
                if i + di < m and j+height < n and matrix[i+di][j+height] == '1':
                    continue
                return False
            for dj in range(height+1):
                if i+height < m and j + dj < n and matrix[i+height][j+dj] == '1':
                    continue
                return False
            self.h = max(self.h, height+1)
            maxS(i,j,height+1)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    self.h = 1 if self.h == 0 else self.h
                    maxS(i,j,1)
        return self.h**2

b = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(b))
