import heapq


class Solution(object):
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		heapq.heapify(nums)
		i= 0
		while i < len(nums) - k:
			heapq.heappop(nums)
		return heapq.heappop(nums)

print(Solution().findKthLargest([3,2,1,5,6,4],4))
