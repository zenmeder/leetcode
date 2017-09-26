#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores, res = [], 0
        for op in ops:
            if op not in ['+', 'C', 'D']:
                scores.append(int(op))
                res += int(op)
            elif op == '+':
                if len(scores) >= 2:
                    scores.append(scores[-1] + scores[-2])
                    res += scores[-1]
                elif len(scores) == 1:
                    scores.append(scores[-1])
                    res += scores[-1]
            elif op == 'C':
                c = scores.pop()
                res -= c
            elif op == 'D' and len(scores) >= 1:
                scores.append(2*scores[-1])
                res += scores[-1]
        return res

print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))