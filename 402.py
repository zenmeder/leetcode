#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        length, i, flag = len(num), 0, 0
        if k==0:
            return num
        if k >= length:
            return 0
        for i in range(length):
            if num[i] == '0':
                flag = 1
                break
        if k >= i and flag:
            if i == length-1:
                return '0'
            return self.removeKdigits(str(int(num[i+1:])), k-i)
        else:
            for j in range(length-1):
                if num[j] > num[j+1]:
                    return self.removeKdigits(num[:j]+num[j+1:], k-1)
            return self.removeKdigits(num[:-1],k-1)

print(Solution().removeKdigits('10',2))




