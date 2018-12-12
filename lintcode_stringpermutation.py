class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        aaa = list(A)
        bbb = list(B)
        if len(aaa) != len(bbb):
            return False

        for item in A:
            if A.count(item) != B.count(item):
                return False

        return True