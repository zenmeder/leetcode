#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import bisect


class Solution(object):
	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		if len(arr) <= k:
			return arr
		p = bisect.bisect_left(arr, x)
		low, high = p - 1, p
		result = []
		while low >= 0 and high < len(arr) and k > 0:
			if abs(arr[low] - x) <= abs(arr[high] - x):
				result.append(arr[low])
				k -= 1
				low -= 1
			else:
				result.append(arr[high])
				k -= 1
				high += 1
		if low <0:
			for num in arr[high:high+k]:
				result.append(num)
		else:
			for num in arr[low-k+1:low+1]:
				result.append(num)
		return sorted(result)

print(Solution().findClosestElements([1,2,3,4,5],4,-3))
