#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		r = set()
		result = []
		nums_length = len(nums)
		if nums_length==0:
			return [[]]
		elif nums_length==1:
			return [[nums[0]]]
		#recursive
		p = self.permuteUnique(nums[:-1])
		for a in p:
			for i in range(len(a)):
				a_copy = a[:]
				a_copy.insert(i,nums[-1])
				r.add(tuple(a_copy))
			a.insert(len(a),nums[-1])
			r.add(tuple(a))

		for b in r:
			result.append(list(b))
		return result
solution = Solution()
print(solution.permuteUnique([1,1,2]))