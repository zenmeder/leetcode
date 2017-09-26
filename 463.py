#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count, edge = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    count += 1
                    if i - 1 in range(len(grid)) and grid[i - 1][j]:
                        edge += 1
                    if i + 1 in range(len(grid)) and grid[i + 1][j]:
                        edge += 1
                    if j - 1 in range(len(grid[0])) and grid[i][j - 1]:
                        edge += 1
                    if j + 1 in range(len(grid[0])) and grid[i][j + 1]:
                        edge += 1
                    print(i,j,count,edge)
        return count * 4 - edge

print(Solution().islandPerimeter([]))
