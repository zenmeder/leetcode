#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        visited, self.height, self.res = {}, 0, 10000
        if not bank:
            return -1
        def mutation(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if count == 1:
                        return False
                    count += 1
            return True if count else False

        def dfs(s):
            if s == end:
                self.res = min(self.res, self.height)
                return True
            for b in bank:
                if b not in visited or not visited[b] and mutation(s, b):
                    self.height += 1
                    visited[b] = True
                    dfs(b)
                    self.height -= 1
                    visited[b] = False
            return self.res if self.res != 10000 else -1
        return dfs(start)

print(Solution().minMutation("AAAACCCC",
"CCCCCCCC",
["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
