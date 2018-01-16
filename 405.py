#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = [str(_) for _ in range(0, 10)] + [chr(_) for _ in range(97, 103)]
        def pToHex(num):
            anw = []
            while True:
                anw.append(digits[num % 16])
                num //= 16
                if num < 16:
                    if num : anw.append(digits[num])
                    break
            return ''.join(anw[::-1])
        if num >= 0:
            return pToHex(num)
        return pToHex(2**32+num)



print(Solution().toHex(-3))