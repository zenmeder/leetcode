#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def __init__(self, arrays):
		list0 = arrays[0]
		for num in range(1,len(arrays)):
			if((arrays[num][0]>list0[0] and arrays[num][-1]<list0[-1]) or (arrays[num][0]<list0[0] and arrays[num][-1]>list0[-1])):
				continue
			self.position = num
			break

	def maxDistance(self, arrays):
		"""
		:type arrays: List[List[int]]
		:rtype: int
		"""
		init_a = arrays[self.position][0] if arrays[self.position][0]<arrays[0][0] else arrays[0][0]
		init_b = arrays[self.position][-1] if arrays[self.position][-1] > arrays[0][-1] else arrays[0][-1]
		# print(init_a,init_b)
		# if self.position+1 < len(arrays):
		# 	for num in range(self.position + 1, len(arrays)):
		# 		init_a = init_a if arrays[num][0] <
input = [
	[1,2,3],
	[4,5],
]
solution = Solution(input)
solution.maxDistance(input)
