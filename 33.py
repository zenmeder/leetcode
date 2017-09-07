#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def search(self, nums, target):
		q = len(nums) - 1
		p = 0
		while q >= p:
			r = p
			s = q
			if q>0 and nums[q - 1] <= nums[q] and nums[q] > target:
				q -= 1
			if p<len(nums)-1 and nums[p + 1] >= nums[p] and nums[p] < target:
				p += 1
			if nums[p] == target:
				return p
			elif nums[q] == target:
				return q
			if p == r and s == q:
				break
		return -1


solution = Solution()
print(solution.search([4,5,6,7,1,2,3,3,4],2))
