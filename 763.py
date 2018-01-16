#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        r = [S.rfind(S[_], _) for _ in range(len(S))]
        res, i = [], 0
        while i < len(S):
            start, end = i, r[i]
            j = start+1
            while j <= end:
               if r[j] > end:
                   end = r[j]
               j+=1
            res.append(end-start+1)
            i = end+1
        return res

print(Solution().partitionLabels(''))
