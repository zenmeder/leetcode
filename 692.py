#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        w, s = Counter(words), ['A' for _ in range(k)]
        w['A'] = 0
        for word in w.keys():
            self.insert(word, w, s)
        return s if len(w)-1 >=k else s[:len(w)-1]
    def insert(self, word, w, s):
        i = 0
        while i < len(s) and (w[word] < w[s[i]] or (w[word] == w[s[i]] and word > s[i])):
            i += 1
        t1 = word
        for j in range(i, len(s)):
            t2 = s[j]
            s[j] = t1
            t1 = t2





print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
