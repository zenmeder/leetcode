#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def countBits(self, num):
		res ,i = [0,1,1,2], 1
		while len(res) <= num:
			res += [res[i], res[i]+1, res[i]+1, res[i]+2]
			i += 1
		return res[:num+1]
print(Solution().countBits(1))