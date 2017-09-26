#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        colors = [[0] * len(grid[0]) for _ in range(len(grid))]
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                if (i - 1 >= 0 and colors[i - 1][j] != 0):
                    colors[i][j] = colors[i - 1][j]
                    continue
                if (j - 1 >= 0 and colors[i][j - 1] != 0):
                    colors[i][j] = colors[i][j - 1]
                    continue
                if (i + 1 < m and colors[i + 1][j] != 0):
                    colors[i][j] = colors[i + 1][j]
                    continue
                if (j + 1 < n and colors[i][j + 1] != 0):
                    colors[i][j] = colors[i][j + 1]
                    continue
                res += 1
                colors[i][j] = res
        return res


print(Solution().numIslands(["111", "010", "111"]))
