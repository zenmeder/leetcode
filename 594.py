#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        c = Counter(nums)
        cache , res = {}, 0
        for num in nums:
            if num not in cache:
                if num+1 in c:
                    res = max(res, c[num]+c[num+1])
        return res


print(Solution().findLHS([1,3,2,2,5,2,3,7]))
