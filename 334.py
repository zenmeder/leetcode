#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		# 遍历数组，记录最小和第二小的数
		#todo
		nums1 = nums2 = None
		for num in nums:
			print(nums1,nums2)
			if nums1 == None:
				nums1 = num
			elif nums2 == None and num>=nums1:
				nums2 = num
			elif num<=nums1:
				nums1,nums2 = num,nums1
			elif nums1<=num<=nums2:
				nums2 = num
			else:
				return True
		return False
solution = Solution()
print(solution.increasingTriplet([2,1,5,0,3]))
