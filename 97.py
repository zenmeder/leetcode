#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isInterleave(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		dps = [[(-1, -1)]]
		if not s1 and not s2 and not s3:
			return True
		if not s3:
			return False
		for i in range(len(s3)):
			tdp = set()
			for dp in dps[-1]:
				if dp[0] < len(s1)-1 and s1[dp[0] + 1] == s3[i]:
					tdp.add((dp[0] + 1, dp[1]))
				if dp[1] < len(s2)-1 and s2[dp[1] + 1] == s3[i]:
					tdp.add((dp[0], dp[1] + 1))
			if not tdp:
				break
			dps.append(tdp)
		else:
			for dp in dps[-1]:
				if dp[0] == len(s1)-1 and dp[1] == len(s2)-1:
					return True
		return False
	# TlE recursion
	def isInterleave1(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		if not s1 and not s2 and not s3:
			return True
		if not s3:
			return False
		if not s1:
			if s2 == s3:
				return True
			return False
		if not s2:
			if s1 == s3:
				return True
			return False
		if s3[0] != s1[0] and s3[0] != s2[0]:
			return False
		elif s3[0] == s1[0] and s3[0] != s2[0]:
			return self.isInterleave(s1[1:], s2, s3[1:])
		elif s3[0] != s1[0] and s3[0] == s2[0]:
			return self.isInterleave(s1, s2[1:], s3[1:])
		else:
			return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])


print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
# print(Solution().isInterleave(
# 	"bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
# 	"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
# 	"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
