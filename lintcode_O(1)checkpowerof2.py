class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if (n < 0 or n==0):
            return False
        if (bin(n).count("1") != 1):
            return False
        return True