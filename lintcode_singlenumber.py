class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        result = 0
        for item in A :
            result = result ^ item
        return result


print (Solution.singleNumber(1,[22,22,1]))