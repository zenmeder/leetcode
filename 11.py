#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxArea(self, height):
		# 暴力求 会超时
		"""
		:type height: List[int]
		:rtype: int
		"""
		area = 0
		for i in range(len(height)):
			if i == len(height) - 1:
				# area = min(height[i],height)
				break
			for j in range(i + 1, len(height)):
				area = max(area, (j - i) * min(height[i], height[j]))
		return area

	def maxArea1(self, height):
		# 先统计出所有可能的最大的maxArea，再取最大值，统计标准为:
		# 取出（i,j)使得i左边没有比height[i]更高的点，j右边也没有比height[j]更高的点
		# ratio:58%
		"""
		:type height: List[int]
		:rtype: int
		"""
		a,b,c,d = [[] for i in range(4)]
		lmax = rmax = 0
		for i in range(len(height)):
			if height[i] < lmax:
				continue
			a.append(i)
			b.append(height[i])
			lmax = max(lmax,height[i])

		for j in range(len(height))[::-1]:
			if height[j] < rmax:
				continue
			c.append(j)
			d.append(height[j])
			rmax = max(rmax,height[j])
		maxArea = 0
		print(a,b,c,d)
		for i in range(len(a)):
			for j in range(len(c)):
				maxArea = max(maxArea,max(a[i]-c[j],c[j]-a[i])*min(b[i],d[j]))
		return maxArea
solution = Solution()
print(solution.maxArea1([5,4,2,3]))
