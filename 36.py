#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isValidSudoku(self, board):
		if len(board) == 0 or len(board[0]) == 0:
			return False
		for i in range(len(board)):
			row = {}
			column = {}
			for j in range(len(board)):
				if board[i][j] != '.' and board[i][j] in row:
					return False
				if board[j][i] != '.' and board[j][i] in column:
					return False
				row[board[i][j]] = 1
				column[board[j][i]] = 1
		# 判断小立方体里是否有重复数
		nodes = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
		for node in nodes:
			cube = {}
			for i in range(3):
				for j in range(3):
					if board[node[0]+i][node[1]+j] != '.' and board[node[0]+i][node[1]+j] in cube:
						return False
					cube[board[node[0]+i][node[1]+j]] = 1
		return True

print(Solution().isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]))