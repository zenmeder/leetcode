#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findLongestWord(self, s, d):
		d = self.bubble_sort(d)
		for word in d:
			if self.intersection(s, word):
				return word
		return ''

	def intersection(self, s1, s2):
		start = 0
		for letter in s2:
			index = s1.find(letter, start)
			if index != -1:
				start = index+1
			else:
				return False
		return True

	def bubble_sort(self, lists):
		# 冒泡排序
		count = len(lists)
		for i in range(0, count):
			for j in range(i + 1, count):
				if len(lists[i]) < len(lists[j]) or (lists[i] > lists[j] and len(lists[i]) == len(lists[j])):
					lists[i], lists[j] = lists[j], lists[i]
		return lists

print(Solution().findLongestWord("aewfafwafjlwajflwajflwafj",
["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]))

print(Solution().intersection('aewfafwafjlwajflwajflwafj','awef'))