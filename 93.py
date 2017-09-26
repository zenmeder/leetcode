#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        length, res= len(s),set()
        for i in range(3):
            if self.isValid(s[:i+1]):
                for j in range(i+1, i+4):
                    if self.isValid(s[i+1:j+1]):
                        for m in range(j+1,j+4):
                            if self.isValid(s[j+1:m+1]):
                                for n in range(m+1,length):
                                    if self.isValid(s[m+1:]):
                                        res.add(s[:i+1]+'.'+s[i+1:j+1]+'.'+s[j+1:m+1]+'.'+s[m+1:])
        return list(res)
    def isValid(self, s):
        if not s:
            return False
        if int(s) > 255:
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        return True
print(Solution().restoreIpAddresses("010010"))

