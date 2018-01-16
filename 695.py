#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            print(i, j)
            color[i][j] = 1
            self.count += 1
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # 4 directions
            for direction in directions:
                if 0 <= i + direction[0] < len(grid) and 0 <= j + direction[1] < len(grid[0]) and \
                        grid[i + direction[0]][j + direction[1]] and not color[i + direction[0]][j + direction[1]]:
                    dfs(i + direction[0], j + direction[1])

        color = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not color[i][j] and grid[i][j]:
                    self.count = 0
                    dfs(i, j)
                    res = max(self.count, res)
        return res


# g = [[0,1,0],[1,1,0],[0,1,1]]
# g = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
g = [[0,0,0,0,0,0,0,0]]

print(Solution().maxAreaOfIsland(g))
