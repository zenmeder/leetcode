#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		previous_sum = []
		for i in range(len(nums) - 2):
			j = i + 1
			k = len(nums) - 1
			while j < k:
				sums = nums[i] + nums[j] + nums[k] - target
				# print(i, j, k,sums)
				if sums == 0:
					return target
				elif sums < 0:
					if len(previous_sum) == 0:
						min_distance = sums
					elif k - j == 1 or previous_sum[-1] < 0:
						min_distance = self.compare(min_distance, sums)
					elif len(previous_sum) != 0 and previous_sum[-1] > 0:
						min_distance = self.compare(min(previous_sum[-1], -sums), min_distance)
					j += 1
					previous_sum.append(sums)
					continue
				elif sums > 0:
					if len(previous_sum) == 0:
						min_distance = sums
					elif k - j == 1 or previous_sum[-1] > 0:
						min_distance = self.compare(min_distance, sums)
					elif previous_sum[-1] < 0:
						min_distance = self.compare(min(previous_sum[-1], -sums), min_distance)
					k -= 1
					previous_sum.append(sums)
					continue
		return min_distance + target

	def postive(self, x):
		return x if x >= 0 else -x

	def compare(self, x, y):
		i = self.postive(x)
		j = self.postive(y)
		return y if i > j else x


print(Solution().threeSumClosest([1, 2, 5, 10, 11], 12))
