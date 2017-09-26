#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, post = [1], [1]
        for i in range(1, len(nums)):
            pre.append(nums[i-1]*pre[-1])
        for i in range(len(nums)-1)[::-1]:
            post.append(nums[i+1]*post[-1])
        post.reverse()
        return [pre[i]*post[i] for i in range(len(nums))]

print(Solution().productExceptSelf([]))