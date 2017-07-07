#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class LogSystem(object):
	def __init__(self):
		self.l = {}

	def put(self, id, timestamp):
		"""
		:type id: int
		:type timestamp: str
		:rtype: void
		"""
		self.l[id] = timestamp

	def retrieve(self, s, e, gra):
		"""
		:type s: str
		:type e: str
		:type gra: str
		:rtype: List[int]
		"""
		if gra == "Year":
			a = 4
		elif gra == "Month":
			a = 7
		elif gra == "Day":
			a = 10
		elif gra == "Hour":
			a = 13
		elif gra == "Minute":
			a = 16
		else:
			a = 19
		s = s[:a]
		e = e[:a]
		result = []
		for (key, value) in self.l.items():
			v = value[:a]
			print(s,v,e)
			if s <= v <= e or e <= v <= s:
				result.append(key)
		return result

obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))
