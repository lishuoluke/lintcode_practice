class Solution:
    """
    @param n: the number n
    @return: the times n convert to 1
    """

    def digitConvert(self, n):
        # Write your code here
        if n == 1:
            return 0
        number = 0
        while (n != 1):
            if n % 2 == 0:
                n = n / 2
                number = number + 1
            else:
                n = 3 * n + 1
                number = number + 1

        return number
