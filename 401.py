#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from itertools import combinations
from functools import reduce
class Solution(object):
	def readBinaryWatch(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		if num == 0: return ["0:00"]
		l = ['00:01', '00:02', '00:04', '00:08', '00:16', '00:32', '1:00','2:00','4:00','8:00']
		c = combinations(l, num)
		result = []
		for t in c:
			time = reduce(self.addTime, t)
			timeH , timeM = time.split(':')
			if int(timeH) < 12 and int(timeM) <= 59:
				timeH = timeH[1] if timeH[0]=='0' and len(timeH) == 2 else timeH
				timeM = '0'+timeM if len(timeM) == 1 else timeM
				time = ':'.join([timeH, timeM])
				result.append(time)
		return sorted(result)


	def addTime(self, a, b):
		ah , am = a.split(':')
		bh , bm = b.split(':')
		result = ':'.join([str(int(ah)+int(bh)), str(int(am)+int(bm))])
		return result
print(Solution().readBinaryWatch(5))