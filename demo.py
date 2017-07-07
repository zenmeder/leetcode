#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
def log(func):
	def wrapper(*args, **kwargs):
		print("call %s()" % func.__name__)
		return func(*args, **kwargs)
	return wrapper()

@log
def hello():
	print('hello')
