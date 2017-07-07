#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def letterCombinations(self, digits):
		# ratio:98.51%
		"""
		:type digits: str
		:rtype: List[str]
		"""
		d = {
			'2':'abc',
			'3':'def',
			'4':'ghi',
			'5':'jkl',
			'6':'mno',
			'7':'pqrs',
			'8':'tuv',
			'9':'wxyz'
		}
		result = []
		for i in range(len(digits)):
			l = d[str(digits[i])]
			if len(result) ==0:
				for j in range(len(l)):
					result.append(l[j])
			else:
				temp_r = []
				for k in range(len(result)):
					for m in range(len(l)):
						temp_r.append(result[k]+l[m])
				result = temp_r[:]
		return result

solution = Solution()
print(solution.letterCombinations('234'))