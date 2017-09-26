#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def maximumSwap(self, num):
        num = list(str(num))
        for i in range(len(num)):
            p = i
            for j in range(i, len(num)):
                if num[j] >= num[p]:
                    p = j
            if num[i] == num[p]:
                continue
            else:
                num[i], num[p] = num[p], num[i]
                break

        return int(''.join(num))


print(Solution().maximumSwap(983688))
