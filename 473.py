#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def makesquare(self, nums):
        c = sum(nums)
        if not nums or c % 4:
            return False
        nums.sort()
        sums = [0,0,0,0]
        self.length = len(nums)
        def dfs(index, target):
            if (index == self.length):
                return True if (sums[0] == target and sums[1] == target and sums[2] == target) else False
            for i in range(4):
                if sums[i] + nums[index] > target: continue
                sums[i] += nums[index]
                if dfs(index+1, target): return True
                sums[i] -= nums[index]
            return False
        return dfs(0, c//4)


print(Solution().makesquare([3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]))
