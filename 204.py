#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# TLE
		if n == 0 or n == 1 or n == 2:
			return 0
		a = [2]
		for i in range(3, n):
			flag = 1
			if i % 2 == 0:
				continue
			for num in a:
				if not i % num:
					flag = 0
					break
			if flag:
				a.append(i)
		return len(a)

	def countPrimes1(self, n):
		if n == 0 or n == 1 or n == 2:
			return 0

		# a = [1 for i in range(n)]
		# for i in range(2,int(math.sqrt(n))+1):
		# 	if self.prime(i):
		# 		for j in range(3,n):
		# 			if j%i == 0:
		# 				a[j] = 0
		# count = 0
		# print(a)
		# for i in range(len(a)):
		# 	if a[i] ==1:
		# 		count+=1
		# return count-1
	def prime(self, n):
		'判断n是否为素数 n>=2'
		if n==2:
			return True
		for i in range(2,int(math.sqrt(n))+1):
			if n%i == 0:
				return False
		return True

solution = Solution()
print(solution.countPrimes1(5))
