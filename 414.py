#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def thirdMax(self, nums):
		if not nums:
			return nums
		p = q = r = None
		for i in range(len(nums)):
			l = [nums[j] for j in [p,q,r] if j!=None]
			if nums[i] in l:
				continue
			if p == None or nums[i] > nums[p]:
				r, q, p = q, p, i
			elif (q == None and nums[i] < nums[p]) or nums[q] < nums[i] < nums[p]:
				r, q = q, i
			elif (r== None and nums[i] < nums[q]) or nums[r] < nums[i] < nums[q]:
				r = i
		return nums[p] if (q==None or r==None) else nums[r]
print(Solution().thirdMax([2,2,3,1]))
