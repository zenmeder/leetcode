#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(_) for _ in range(1, n+1)]
        res, i = '', 1
        while len(nums) != 1:
            pos = (k-1)//factorial(n-i) if (k-1)//factorial(n-i) < len(nums) else len(nums)-1
            k-=pos*factorial(n-i)
            s = nums[pos]
            res += s
            nums.remove(s)
            i += 1
        res += nums[0]
        return res


print(Solution().getPermutation(9,2))
