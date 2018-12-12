class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        A = []
        for i in range(1, n + 1):
            if (i % 15 == 0):
                A.append("fizz buzz")
            elif (i % 3 == 0):
                A.append("fizz")
            elif (i % 5 == 0):
                A.append("buzz")
            else:
                A.append(str(i))
        return A