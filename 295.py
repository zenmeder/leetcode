class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.l:
            self.l.append(num)
        else:
            i, j = 0, self.length-1
            while i<=j:
                mid = (i+j)//2
                if self.l[mid] <= num:
                    i = mid+1
                else:
                    j = mid-1
            self.l.insert(i, num)
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length%2:
            print(self.l[(self.length-1)//2])
            return self.l[(self.length-1)//2]
        else:
            print((self.l[self.length//2]+self.l[self.length//2-1])/2)
            return (self.l[self.length//2]+self.l[self.length//2-1])/2

a = MedianFinder()
a.addNum(1)
a.addNum(2)
print(a.findMedian())