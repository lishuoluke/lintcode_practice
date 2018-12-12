class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        if (n < 4 and n != 1):
            return False
        else:
            if (n == 1):
                return True
            else:
                while (n > 3):
                    sum = 0
                    hehe = [int(i) for i in str(n)]
                    for item in hehe:
                        sum = item * item + sum
                    n = sum
                    if (n == 4):
                        return False

            if (sum == 1):
                return True
            else:
                return False