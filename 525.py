class Solution(object):
	def findMaxLength(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		res, s, d = 0, 0, {}
		if len(nums) < 2:
			return 0
		for i in range(len(nums)):
			s = s + 1 if nums[i] else s - 1
			if s == 0:
				res = max(i+1,res)
			elif s not in d:
				d[s] = i
			else:
				res = max(res, i-d[s])
		return res


print(Solution().findMaxLength([0,1,1,0,1,1,0,0,1]))