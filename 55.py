#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def __init__(self):
		self.dp = [1]

	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		#TLE
		if len(nums) == 0:
			return False
		if len(nums) == 1:
			return True
		if len(nums) == 2 and nums[0] > 0:
			return True
		elif len(nums) == 2 and nums[0] == 0:
			return False
		dp = self.dp
		if nums[0] > 0:
			dp.append(1)
		for i in range(2, len(nums)):
			flag = 1
			for j in range(len(dp)):
				if dp[j] == 1 and nums[j] >= i - j:
					dp.append(1)
					flag = 0
					break
			if flag:
				dp.append(0)
		return True if dp[-1] else False
	def canJump2(self, nums):
		color = [0 for i in range(len(nums))]
		color[0] = 1
		for i in range(len(nums)):
			if color[i] == 1 :
				if i>=1 and color[i-1]==1 and nums[i-1]-nums[i]>=1:
					continue
				color[i+1:i+nums[i]+1] = [1 for j in range(nums[i])]
		return True if color[-1] else False

solution = Solution()
# print(solution.canJump2([2,3,1,1,4]))
print(solution.canJump2([2,3,1,1,4]))