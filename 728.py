#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDividingNumbers(num):
            for i in [int(_) for _ in str(num)]:
                if i == 0 or num % i:
                    return False
            return True
        res = []
        for i in range(left, right+1):
            if isDividingNumbers(i):
                res.append(i)
        return res

print(Solution().selfDividingNumbers(1,22))