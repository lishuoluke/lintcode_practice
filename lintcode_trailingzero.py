class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
    # write your code here, try to do it without arithmetic operators.
        trailing = 0
        power = 1
        while (n >= 5 ** power):
            trailing = trailing + int (n/(5 ** power))
            power = power +1
        return trailing