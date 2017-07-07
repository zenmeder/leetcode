#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def maximumProduct(self, nums):
		# 取最大的三个正数or最大的一个正数和绝对值最大的两个负数，再取它们的最大值
		nums.sort(reverse=True)
		max1 = nums[0]*nums[1]*nums[2]
		max2 = nums[0]*nums[-1]*nums[-2]
		return max(max1,max2)
solution = Solution()
print(solution.maximumProduct([-7,-2,3,1,4]))