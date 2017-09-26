#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def makesquare(self, nums):
        if not nums:
            return False
        nums = sorted(nums)
        length, perimeter, count = 0, 0, 0
        for num in nums:
            length += 1
            perimeter += num
        if perimeter % 4:
            return False
        edge, i, j = perimeter // 4, 0, length-1
        while count < 4:
            long = nums[j]
            if long > edge:
                return False
            short = edge - long
            while short > 0:
                short -= nums[i]
                i += 1
            if short < 0:
                return False
            count += 1
            j -= 1
        return True if i-j else False

print(Solution().makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))