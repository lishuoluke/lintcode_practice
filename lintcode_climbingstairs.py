class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here

        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            a = 1
            b = 2
            number = 0
            for i in range(0, n - 2):
                number = a + b
                a = b
                b = number

        return number
