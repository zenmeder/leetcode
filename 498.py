#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        orientation, res = True, []
        m, n = len(matrix), len(matrix[0])
        for i in range(m + n - 1):
            for j in range(m):
                print(i + j + 1 - m, i-j)
                res.append(matrix[m - 1 - j][i + j + 1 - m]) if orientation else res.append(matrix[j][i - j])
            orientation = not orientation
        return res
print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

