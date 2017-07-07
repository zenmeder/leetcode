#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		d = dict()
		for i in range(length):
			if nums[i] in d:
				del d[nums[i]]
			else:
				d[nums[i]] = 1
		return d.popitem()[0]
	def singleNumber2(self,nums):
		# 两个相同的数异或的结果是0，所有的数两两异或，最后结果必然是不同的那个数
		# 空间复杂度减小，但是用时较长
		result = 0
		for num in nums:
			result ^= num
		return result
solution = Solution()
print(solution.singleNumber2([1,2,2,2]))