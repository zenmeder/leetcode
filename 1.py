#coding:utf-8
#!/usr/local/bin/ python3
class Solution(object):
    def twoSum(self, nums, target):
        """
        nums是输入的数组，target是所求的和
        这里的算法核心思想是：对于nums进行一次扫描，我们这里建了一个dict，扫描到数nums[i]时，如果target-nums[i]在dict里，就达到
        了我们的目的，如果没有，就把nums[i]放入dict中。
        ratio: 86.33%
        :param nums:
        :param target:
        :return:
        """
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return [dict[target-nums[i]], i]
            dict[nums[i]] = i
    def twoFlag(self, nums, target):
        """
        两个指针扫描数组，要求数组为顺序排列
        :param nums:
        :param target:
        :return:
        """
        a = 0
        b = len(nums) - 1
        while 1 :
            if(a > len(nums) or b < 0):
                return "FAILED"
            if(nums[a]+nums[b] == target):
                return [min(a,b),max(a,b)]
            if(nums[a]+nums[b] > target):
                b -= 1
            if(nums[a]+nums[b] < target):
                a += 1
solution = Solution()
nums = [-1,-2,-3,-4,-5]
target = -8
print(solution.twoSum(nums, target))
print(solution.twoFlag(nums, target))

