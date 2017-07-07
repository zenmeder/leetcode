#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import time
class Solution(object):
	def subsets(self, nums):
		# result = []
		# stop = len(nums)
		# for i in range(len(nums)-1)[::-1]:
		# 	result += self.sub(nums,i)
		return self.sub(nums, len(nums) - 1)

	def sub(self, nums, stop):
		result = []
		if stop == 0:
			return [[],[nums[0]]]
		else:
			a = self.sub(nums, stop - 1)
			b = a[:]
			for element in a:
				b.append(element + [nums[stop]])
			return b
	def sub1(self,nums):
		# much faster than above when len(nums) is high
		result = []
		for i in range(2**len(nums)):
			a = bin(i)[2:]
			b = []
			print(a)
			for j in range(len(a))[::-1]:
				if int(a[len(a)-1-j])&1:
					print('j',j)
					b.append(nums[j])
			result.append(b)
			print(result)
		return result
solution = Solution()
# a = time.clock()
# print(solution.subsets([i for i in range(3)]))
# print(time.clock()-a)
a = time.clock()
print(solution.sub1([1,2,3,4]))
print(time.clock()-a)
