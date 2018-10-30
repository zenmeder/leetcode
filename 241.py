# -*- coding: utf-8 -*-
"""
 @date: 2018/8/13
 @author: zhaoyu
 @time: 2018-08-13
 @contact: zhaoyu.william@bytedance.com
"""
import pandas as pd
import numpy as np


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        numbers = re.findall('(\d+)', x)
        operations = re.findall('[+*-]',x)
        dp = []
        for i in range(len(numbers)):
            if not i:
                dp.append([numbers[i]])
                continue
            if i==1:
                dp.append([eval(numbers[i-1]+operations[i-1]+numbers[i])])
                continue
            tmp = []