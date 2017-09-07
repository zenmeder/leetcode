#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def minSubArrayLen(self, s, nums):
		if not s:
			return 0
		stop = []
		for i in range(len(s)):
			if i == 0:
				sum = s[i]
				j = i
				while sum < nums and j < len(s)-1:
					j += 1
					sum += s[j]
					if sum >= nums:
						break
				if sum<nums:
					return 0
				minLength = j + 1
				stop.append(j)
			else:
				sum -= s[i - 1]
				k = stop[i - 1]
				while sum < nums and k < len(s) - 1:
					k += 1
					sum += s[k]
				if sum < nums:
					return minLength
				else:
					minLength = min(minLength, k - i + 1)
					stop.append(k)
		return minLength


print(Solution().minSubArrayLen([1,1], 3))
