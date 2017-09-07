#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from collections import Counter


class Solution(object):
	def originalDigits(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		c = Counter(s)
		result = []
		if 'z' in c:
			result += ['0'] * (c['z'])
			d = c['z']
			for letter in 'zero':
				c[letter] -= d
		if 'w' in c:
			result += ['2'] * (c['w'])
			d = c['w']
			for letter in 'two':
				c[letter] -= d
		if 'u' in c:
			result += ['4'] * (c['u'])
			d = c['u']
			for letter in 'four':
				c[letter] -= d
		if 'x' in c:
			result += ['6'] * (c['x'])
			d = c['x']
			for letter in 'six':
				c[letter] -= d
		if 'g' in c:
			result += ['8'] * (c['g'])
			d = c['g']
			for letter in 'eight':
				c[letter] -= d
		if 'o' in c and c['o'] != 0:
			result += ['1'] * (c['o'])
			d = c['o']
			for letter in 'one':
				c[letter] -= d
		if 't' in c and c['t'] != 0:
			result += ['3'] * (c['t'])
			d = c['t']
			for letter in 'three':
				c[letter] -= d
		if 'f' in c and c['f'] != 0:
			result += ['5'] * (c['f'])
			d = c['f']
			for letter in 'five':
				c[letter] -= d
		if 's' in c and c['s'] != 0:
			result += ['7'] * (c['s'])
			d = c['s']
			for letter in 'seven':
				c[letter] -= d
		if 'e' in c and c['e'] != 0:
			result += ['9'] * (c['e'])
			d = c['e']
			for letter in 'nine':
				c[letter] -= d
		result.sort()
		return ''.join(result)

print(Solution().originalDigits('owoztneoer'))
