#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findRestaurant(self, list1, list2):
		"""
		:type list1: List[str]
		:type list2: List[str]
		:rtype: List[str]
		"""
		dict1 = {i:j for j,i in enumerate(list1)}
		dict2 = {i:j for j,i in enumerate(list2)}
		a,b = float('inf'),[]
		for restaurant in dict1:
			if restaurant in dict2:
				if dict1[restaurant]+dict2[restaurant] < a:
					a = dict1[restaurant]+dict2[restaurant]
					b = [restaurant]
				elif dict1[restaurant]+dict2[restaurant] == a:
					b.append(restaurant)

		return b
