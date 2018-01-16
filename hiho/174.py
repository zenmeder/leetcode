#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# class Solution:
#     def dicePossibility(self, n, m):
#         dp = [[0 for _ in range(6*n)] for __ in range(n)]
#         for i in range(n):
#             for j in range(6 * i + 6):
#                 if i == 0:
#                     dp[i][j] = 1 if j < 6 else 0
#                 else:
#                     for k in range(j):
#                         if j - k <= 6:
#                             dp[i][j] += dp[i - 1][k]
#         times = dp[-1][m-1] * 100
#         a = 6 ** n
#         return float('%.2f' % (times/a))
#
#
# print(Solution().dicePossibility(2, 10))
# while True:
#     try:
#         (n, m) = (int(x) for x in input().split())
#         dp = [[0 for _ in range(6*n)] for __ in range(n)]
#         for i in range(n):
#             for j in range(6 * i + 6):
#                 if i == 0:
#                     dp[i][j] = 1 if j < 6 else 0
#                 else:
#                     for k in range(j):
#                         if j - k <= 6:
#                             dp[i][j] += dp[i - 1][k]
#         times = dp[-1][m-1] * 100
#         a = 6 ** n
#         print(float('%.2f' % (times/a)))
#     except EOFError:
#         break
print(float('%.2f'%float(2.00)))
import decimal
a = decimal.Decimal('0.00')
print(a)