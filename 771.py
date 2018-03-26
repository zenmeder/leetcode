#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = Counter(J)
        S = Counter(S)
        anw = 0
        for letter in S:
            if letter in J:
                anw += S[letter]
        return anw


print(Solution().numJewelsInStones('',''))