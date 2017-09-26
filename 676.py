#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.d = dict
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for w in self.d:
            if self.isFind(w, word):
                return True
        return False
    def isFind(self, s1, s2):
        count, i= 0, 0
        while i<len(s1) and i<len(s2):
            if s1[i] != s2[i]:
                count += 1
        if count != 1 or (len(s1) != len(s2)):
            return False
        return True

