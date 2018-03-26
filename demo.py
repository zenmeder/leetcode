def cut(n, prices):
    dp = [prices[0]]
    for i in range(2, n + 1):
        p = prices[i - 1]
        for j in range(len(dp)):
            p = max(p, dp[j] + prices[i - j - 2])
        dp.append(p)
    return dp


def longest(s1, s2):
    dp = [[0 for i in range(len(s2))] for j in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 or j == 0:
                print(s1[0] in s2)
                dp[i][j] = 1 if s1[0] in s2 or s2[0] in s1 else 0
                continue
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp


# print(longest('abcbdab','bdcaba'))

def palindrome(s):
    dp = [[1 for _ in range(len(s))] for __ in range(len(s))]
    for i in range(len(s)):
        for j in range(i)[::-1]:
            if s[i] == s[j]:
                dp[j][i] = 2 + dp[j + 1][i - 1] if j + 1 <= i - 1 else 2
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
    return dp


# print(palindrome('character'))

value = [990, 436, 673, 58, 897]
weight = [144, 487, 210, 567, 1056]


def bag(n):
    dp = [[0 for _ in range(n + 1)] for __ in range(len(weight))]
    for i in range(len(weight)):
        for j in range(n + 1):
            dp[i][j] = 0 if i == 0 else dp[i - 1][j]
            if j >= weight[i - 1] and i > 0:
                dp[i][j] = max(dp[i - 1][j - weight[i - 1]] + value[i-1], dp[i - 1][j])
    return dp[-1][-1]


print(bag(1000))


def p(s):
    dp = [[0 for _ in range(len(s))] for __ in range(len(s))]
    res = 0
    for i in range(len(s)):
        for j in range(i + 1):
            if s[i] == s[j]:
                if j + 1 <= i - 1 and dp[j + 1][i - 1] != 0:
                    dp[j][i] = 2 + dp[j + 1][i - 1]
                elif i == j:
                    dp[j][i] = 1
                elif i - j == 1:
                    dp[j][i] = 2
                res = max(res, dp[j][i])
    return res

def quicksort(s, low, high):
    if low >= high:
        return s
    i, pivot = low-1, s[high]
    for j in range(low, high):
        if s[j] <= pivot:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1], s[high] = s[high], s[i+1]
    quicksort(s, low, i)
    quicksort(s, i+2, high)
    return s

print(quicksort([1,3,2,5,1,0,-3,4,-8],0,8))
