class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalindrome(s):
            return s == s[::-1]

        def getPalindromeSeq(s):
            res = set()
            if isPalindrome(s):
                res.add(tuple([s]))
            for i in range(1, len(s)):
                if isPalindrome(s[:i]) and isPalindrome(s[i:]):
                    res.add(tuple([s[:i], s[i:]]))
                    for seq in getPalindromeSeq(s[:i]):
                        res.add((seq+tuple(s[i:])))
                    for seq in getPalindromeSeq(s[i:]):
                        res.add((tuple(s[:i])+seq))
                elif isPalindrome(s[:i]) and not isPalindrome(s[i:]):
                    for seq in getPalindromeSeq(s[:i]):
                        res.add(seq+tuple([_ for _ in s[i:]]))
                elif not isPalindrome(s[:i]) and isPalindrome(s[i:]):
                    for seq in getPalindromeSeq(s[i:]):
                        res.add(tuple([_ for _ in s[:i]])+seq)
                else:
                    res.add(tuple([_ for _ in s]))
            return res
        res = []
        for _ in getPalindromeSeq(s):
            res.append(list(_))
        return res

print(Solution().partition('aba'))