#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        w1, w2 = words1.split(), words2.split()
        if len(w1) != len(w2): return False
        for i in range(len(w1)):
            if w1[i] == w2[i] or [w1[i],w2[i]] in pairs or [w2[i],w1[i]] in pairs:
                continue
            return False
        return True