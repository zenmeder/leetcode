class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 0:
			return []
		if len(nums) == 1:
			return [[nums[0]]]
		# if len(nums) == 2:
		# 	return [[nums[0],nums[1]],[nums[1],nums[0]]]
		last = self.permute(nums[:-1])
		result = []
		for l in last:
			for i in range(len(l)):
				li = l[:]
				li.insert(i, nums[-1])
				result.append(li)
			l.insert(len(l), nums[-1])
			result.append(l)
		return result


solution = Solution()
print(solution.permute([1, 2, 3]))
