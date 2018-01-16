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
        def dfs(i,j):
            color[i][j] = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for direction in directions:
                if 0 <= i + direction[0] < len(grid) and 0 <= j + direction[1] < len(grid[0]) and \
                        grid[i + direction[0]][j + direction[1]] == '1' and not color[i + direction[0]][j + direction[1]]:
                    dfs(i + direction[0],j + direction[1])
        color = [[0] * len(grid[0]) for _ in range(len(grid))]
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not color[i][j]:
                    dfs(i,j)
                    res += 1
        return res


g = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().numIslands(g))
