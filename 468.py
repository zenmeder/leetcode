#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def validIPAddress(self, IP):
		"""
		:type IP: str
		:rtype: str
		"""
		if self.isIPV4(IP):
			return "IPv4"
		elif self.isIPV6(IP):
			return "IPv6"
		else:
			return "Neither"

	def isIPV4(self, IP):
		ip = IP.split('.')
		if len(ip) != 4:
			return False
		for num in ip:
			if '0' <= num <= '255' and (num[0] != '0' or num == '0') and len(num) <= 3:
				continue
			else:
				return False
		return True

	def isIPV6(self, IP):
		ip = IP.split(':')
		if len(ip) != 8:
			return False
		for num in ip:
			print(num)
			if '0' <= num.upper() <= 'FFFF' and len(num) <= 4:
				continue
			else:
				return False
		return True


print(Solution().validIPAddress("192.0.0.1"))
