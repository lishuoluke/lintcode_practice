class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A ==[]:
            return 0
        for i in range (0,len(A)) :
            if A[i] == target :
                return i
        if A[0] > target :
                return 0
        if A[len(A)-1] < target :
                return len(A)
        for j in range (1,len(A)-1) :
            if (target > A[j] and target <A[j+1]):
                return j+1