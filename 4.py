#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		# 对两个数组分别取一个指针，扫描到中位数的个数后停止。
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		:grade: 83.18%
		"""
		median1 = int((len(nums1) + len(nums2) + 1) / 2)
		median2 = -1 if (len(nums1) + len(nums2)) % 2 else median1 + 1
		f1 = f2 = -1
		count = 0
		while 1:
			if f1 == len(nums1) - 1:
				move = 2
			elif f2 == len(nums2) - 1:
				move = 1
			else:
				move = 1 if nums1[f1 + 1] < nums2[f2 + 1] else 2
			if move == 1:
				f1 += 1
			elif move == 2:
				f2 += 1
			count += 1
			if count == median1:
				median1_value = nums1[f1] if move == 1 else nums2[f2]
				if median2 == -1:
					return median1_value
				else:
					if f1 == len(nums1) - 1:
						move = 2
					elif f2 == len(nums2) - 1:
						move = 1
					else:
						move = 1 if nums1[f1 + 1] < nums2[f2 + 1] else 2
					median2_value = nums1[f1 + 1] if move == 1 else nums2[f2 + 1]
					return (float)(median1_value + median2_value) / 2


solution = Solution()
nums1 = [1, 2]
nums2 = [3, 4]

print(solution.findMedianSortedArrays(nums1, nums2))
