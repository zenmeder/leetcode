#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res, length= [], len(nums)
        for n in findNums:
            post = -1
            for i in range(length)[::-1]:
                if nums[i] == n:
                    res.append(post)
                elif nums[i] > n:
                    post = nums[i]
        return res

print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))
