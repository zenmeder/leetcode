#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def nextGreaterElements(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return nums
		nums.insert(0, nums[-1])
		res, l ,length = [], [], len(nums)
		mark = []
		for i in range(length)[::-1]:
			if not l:
				l.append(nums[i])
				res.append(-1)
			elif nums[i] < nums[i+1]:
				res.append(nums[i+1])
				l = [nums[i]]+l
			else:
				low, high = 0, len(l)-1
				while low <= high:
					mid = (low+high)//2
					if l[mid] <= nums[i]:
						low = mid+1
					else:
						high = mid-1
				if low >= len(l):
					res.append(-1)
					l = [nums[i]]
					mark.append(i)
				else:
					res.append(l[low])
					l = [nums[i]] + l[low:]
		res.reverse()
		for m in mark:
			if nums[m] != l[-1]:
				for a in l:
					if a > nums[m]:
						res[m] = a
						break
		res = res[1:-1]+[res[0]]
		return res
print(Solution().nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100]))