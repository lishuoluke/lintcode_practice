class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        if triangle == None:
            return 0
        if len(triangle) == 1 and len(triangle[0]) == 1:
            return triangle[0][0]
        length = len(triangle)
        for i in range(1, length):
            for j in range(0, len(triangle[i])):
                if (j == 0):
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
                elif (j == len(triangle[i]) - 1):
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j - 1], triangle[i - 1][j])

        minimum = 20000000
        for item in triangle[length - 1]:
            if item < minimum:
                minimum = item

        return minimum
