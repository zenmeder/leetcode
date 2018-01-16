#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def canPartition(self, nums):
        #dfs time limited
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nums.sort()
        s = sum(nums)
        if s % 2: return False
        def dfs(i,cumsum,target):
            if cumsum == target:
                return True
            if i == len(nums)-1:
                return True if cumsum == target else False
            for j in range(i+1, len(nums)):
                if nums[j] + cumsum > target:
                    break
                elif nums[j] + cumsum == target:
                    return True
                else:
                    cumsum += nums[j]
                    if dfs(j, cumsum, target): return True
                    cumsum -= nums[j]
            return False
        return dfs(0,nums[0],s//2)

print(Solution().canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]))

