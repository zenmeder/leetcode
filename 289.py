#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in zip(dx, dy):
                    i, j = i + x, j + y
                    if 0 <= i < m and 0 <= j < n and (board[i][j] == 1 or board[i][j] == 2):
                        count += 1
                if board[i][j] and (count < 2 or count > 3):
                    board[i][j] = 2
                elif (not board[i][j] and board[i][j] == 3):
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2

