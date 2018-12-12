class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        strings = ''
        for i in range (0,n+1):
            strings = strings + str(i)
        return strings.count (str(k))
