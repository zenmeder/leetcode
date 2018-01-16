#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

def nxt(s):
    next, k = [-1], -1
    for q in range(1, len(s)):
        while k > -1 and s[k + 1] != s[q]:
            k = next[k]
        if s[k + 1] == s[q]:
            k += 1
        next.append(k)
    return next


def kmp(s1, s2):
    next, k = nxt(s2), -1
    count = 0
    for i in range(len(s1)):
        while k > -1 and s2[k + 1] != s1[i]:
            k = next[k]
        if s2[k + 1] == s1[i]:
            k += 1
        if k == len(s2) - 1:
            count += 1
            k = -1
            i = i-len(s2)+2
    return count


print(kmp('ababa', 'aba'))
