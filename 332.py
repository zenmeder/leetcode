class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        used, anw = set(), ['JFK']

        def getAnw(dp):
            tmpdp, n = 'ZZZ', -1
            for i in range(len(tickets)):
                if i not in used:
                    if tickets[i][0] == dp:
                        if tmpdp > tickets[i][1]:
                            tmpdp, n = tickets[i][1], i
            if n >=0:
                used.add(n)
                anw.append(tmpdp)
                getAnw(tmpdp)
        getAnw('JFK')
        return anw

a = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(a))
