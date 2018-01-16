#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        for i in range(len(words1)):
            if not self.isSimilar(words1[i], words2[i],pairs):
                return False
        return True

    def isSimilar(self, s1, s2, pairs):
        for pair in pairs:
            if (pair[0] == s1 and pair[1] == s2) or (pair[0] == s2 and pair[1] == s1):
                return True
            elif pair[0] == s1:
                self.isSimilar(pair[1], s2, pairs)
            elif pair[1] == s1:
                self.isSimilar(pair[0],s2, pairs)
        return False

print(Solution().areSentencesSimilarTwo(["great", "acting", "skills"],["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]))