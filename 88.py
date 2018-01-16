#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        low = None
        for i in range(n):
            low, high = 0 if not low else low, m + i - 1
            while low <= high:
               mid = (low+high)//2
               if nums1[mid] < nums2[i]:
                   low = mid + 1
               else:
                   high = mid - 1
            nums1.insert(low, nums2[i])
        return nums1

print(Solution().merge([0],0,[2,4,6,9],4))