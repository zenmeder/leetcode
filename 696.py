#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) < 2:
            return 0
        n, count, i = len(s), 0, 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            if j == n:
                break
            k = j + 1
            while k < n and s[k] == s[j]:
                k += 1
            count += min(j-i,k-j)
            i = j
        return count


print(Solution().countBinarySubstrings(
        "00110"))
