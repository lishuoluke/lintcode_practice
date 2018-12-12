class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        aaa = list(A)
        bbb = list(B)
        for item in B:
            if (A.count(item) >= B.count(item)):
                continue
            else:
                return False

        return True