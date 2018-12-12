class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        p, q, k = m - 1, n - 1, m + n - 1
        while p >= 0 and q >= 0:
            if A[p] > B[q]:
                A[k] = A[p]
                p, k = p - 1, k - 1
            else:
                A[k] = B[q]
                q, k = q - 1, k - 1

        A[:q + 1] = B[:q + 1]