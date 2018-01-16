#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
    def subarraySum(self, nums, k):
        def cumsum(nums, low, high, k):
            if low > high:
                return 0
            if low == high:
                return 1 if nums[low] == k else 0
            mid, res = (low + high) // 2, 0
            # 找出通过mid的值为k的子数组
            left, right = {}, {}
            lc, rc = None, None
            for i in range(low, mid)[::-1]:
                lc = nums[i] if not lc else lc + nums[i]
                left[lc] = 1 if lc not in left else left[lc] + 1
                if lc + nums[mid] == k:
                    res += 1
            for j in range(mid + 1, high + 1):
                rc = nums[j] if not rc else rc + nums[j]
                right[rc] = True
                if rc + nums[mid] == k:
                    res += 1
                if k - rc - nums[mid] in left:
                    res += left[k - rc - nums[mid]]

            if nums[mid] == k:
                res += 1
            l, r = cumsum(nums, low, mid - 1, k), cumsum(nums, mid + 1, high, k)
            res = res + l + r
            return res

        return cumsum(nums, 0, len(nums) - 1, k)


solution = Solution()
print(solution.subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
