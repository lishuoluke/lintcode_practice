class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """

    def checkSumOfSquareNumbers(self, num):
        # write your code here
        if (num < 0):
            return False

        for item1 in range(0, int(num ** 0.5) + 1):

            if ((num - item1 * item1) ** 0.5 == int((num - item1 * item1) ** 0.5)):
                return True

        return False