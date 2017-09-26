#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        numbers = set()
        for num in nums:
            if not numbers:
                numbers.add(num)
                continue
            a = numbers.copy()
            for number in numbers:
                a.add(number+num)
            numbers = a.copy()
            numbers.add(num)
            if target in numbers:
                return True
        return False

print(Solution().canPartition([1]))