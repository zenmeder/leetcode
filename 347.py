#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		# 先对元素以及其出现的次数进行统计
		hash_times = {}
		for i in range(len(nums)):
			if nums[i] in hash_times:
				hash_times[nums[i]] += 1
			else:
				hash_times[nums[i]] = 1
		list_times = [0 for i in range(len(nums) + 1)]
		for num, times in hash_times.items():
			if list_times[times] == 0:
				list_times[times] = [num]
			else:
				list_times[times].append(num)
		# 从大到小依次读k个
		i = len(list_times) - 1
		count = 0
		res = []
		while i > 0 and count < k:
			if list_times[i] == 0:
				i -= 1
				continue
			else:
				res += list_times[i]
				count += len(list_times[i])
				i -= 1
		if count <= k:
			return res
		else:
			return res[:k]

print(Solution().topKFrequent([1,2,3,4,5,6], 5))
