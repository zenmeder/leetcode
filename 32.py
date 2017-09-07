class Solution:
	# @param s, a string
	# @return an integer
	def longestValidParentheses(self, s):
		stack = []
		match = [0 for i in range(0, len(s))]
		for i, c in enumerate(s):
			if c == '(':
				stack.append(i)
			elif c == ')' and len(stack) != 0:
				match[i] = match[stack[-1]] = 1
				stack.pop()

		ans, temp = 0, 0
		for i, c in enumerate(match):
			if match[i]:
				temp = temp + 1
				ans = max(ans, temp)
			else:
				temp = 0
		return ans