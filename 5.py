#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
class Solution(object):
	def longestPalindrome(self, s):
		# 复杂度n^2
		# 分奇数和偶数情况讨论
		"""
		:type s: str
		:rtype: str
		"""
		# ratio: 38%
		# 奇数回文串的情况
		if s == '' or len(s) == 1:
			return s
		maxLength1 = 0
		for i in range(len(s)):
			length = 1
			if i == 0 or i == len(s) - 1:
				continue
			else:
				j = i - 1
				k = i + 1
				while 1:
					if j == -1 or k == len(s):
						break
					if s[j] == s[k]:
						length += 2
					else:
						break
					j -= 1
					k += 1
				if length > maxLength1:
					flag1 = i
				maxLength1 = max(maxLength1, length)
		# return maxLength1
		# 偶数回文串的情况
		maxLength2 = 0
		for i in range(len(s)):
			length = 0
			if i == len(s) - 1:
				break
			if s[i + 1] != s[i]:
				continue
			else:
				length = 2
				j = i - 1
				k = i + 2
				while 1:
					if j == -1 or k == len(s):
						break
					if s[j] == s[k]:
						length += 2
					else:
						break
					j -= 1
					k += 1
				if length > maxLength2:
					flag2 = i
				maxLength2 = max(length, maxLength2)
		if maxLength1 > maxLength2:
			return s[int(flag1 - (maxLength1 - 1) / 2):int(flag1 + (maxLength1 - 1) / 2 + 1)]
		else:
			return s[int(flag2 - maxLength2 / 2 + 1):int(flag2 + maxLength2 / 2 + 1)]

	def longestPalindrome1(self, s):
		# 动态规划
		dp = [[False for i in range(len(s))] for i in range(len(s))]
		# print(dp)
		maxlength = 0
		for i in range(len(s)):
			j = i
			while j >= 0:
				if s[j] == s[i] and (i - j < 2 or dp[i - 1][j + 1] == True):
					dp[i][j] = True
					if i - j + 1 > maxlength:
						maxlength = i - j + 1
						a = i
						b = j
				j -= 1
		return s[b:a+1]

	def longestPalindrome2(self, s):
		"""
        :type s: str
        :rtype: str
        """
		n = len(s)
		if n <= 1:
			return s
		dp = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
		m, res = 0, ''
		for i in range(n):
			for j in range(i):
				if s[j] == s[i]:
					dp[j][i] = 2 + dp[j + 1][i - 1] if j + 1 <= i - 1 else 2
				else:
					dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
				if dp[j][i] > m:
					if i - j + 1 == dp[j][i]:
						res = s[j:i + 1]
					m = dp[j][i]
		return res
solution = Solution()
print(solution.longestPalindrome2('ab'))
