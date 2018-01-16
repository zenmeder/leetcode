#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wd = {_:True for _ in words}
        letters = [chr(97+_) for _ in range(26)]
        def dfs(w):
            for c in letters:
                if w+c in wd:
                    self.l = w+c if len(self.l) < len(w+c) or (len(self.l) == len(w+c) and  w+c<self.l) else self.l
                    dfs(w+c)
        self.l = None
        for word in words:
            if len(word) == 1:
                self.l = word if not self.l else self.l
                dfs(word)
        return self.l
print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))


