#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        anwser, length = None, float('inf')
        def match(s1, s2):
            s1 = Counter([_.lower() for _ in s1 if _.isalpha()])
            s2 = Counter(s2)
            for letter in s1:
                if letter not in s2 or s2[letter] < s1[letter]:
                    return False
            return True
        for word in words:
            if len(word) < length:
                if match(licensePlate, word):
                    anwser = word
                    length = len(anwser)
        return anwser

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(Solution().shortestCompletingWord(licensePlate, words))

