class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if (matrix == []):
            return False
        numrows = len(matrix)  # 3 rows in your example
        numcols = len(matrix[0])
        for i in range(0, numrows):
            for j in range(0, numcols):
                if (matrix[i][j] == target):
                    return True

        return False