#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def combination(k, n, l):
            res = []
            if k==1:
                return [l+[n]] if n not in l and n in range(1, 10) and n < l[-1] else []
            for i in range(1, 10):
                if i in l or (l and i >= l[-1]):
                    continue
                c = combination(k-1, n-i, l +[i])
                if c:
                    for t in c:
                        res.append(t)
            return res
        return combination(k,n,[])

print(Solution().combinationSum3(3,7))