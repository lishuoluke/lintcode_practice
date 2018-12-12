class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        Matrix = [[0 for x in range(m)] for y in range(n)]

        for i in range(0, n):
            Matrix[i][0] = 1
        for j in range(0, m):
            Matrix[0][j] = 1

        for i1 in range(1, n):
            for j1 in range(1, m):
                Matrix[i1][j1] = Matrix[i1 - 1][j1] + Matrix[i1][j1 - 1]

        return Matrix[n - 1][m - 1]

