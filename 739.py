#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # brute solution
        res, flag = [], 0
        for i in range(len(temperatures)):
            for k in range(i)[::-1]:
                if temperatures[k] >= temperatures[i]:
                    flag = 1 if temperatures[k] == temperatures[i] else 2
                    break
            if flag != 1:
                for j in range(i + 1, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        res.append(j - i)
                        break
                else:
                    res.append(0)
            else:
                res.append(res[k]+k-i if res[k] else res[k])

        return res
a = [34,80,80,34,34,80,80,80,80,34]
print(Solution().dailyTemperatures(a))
