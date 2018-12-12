def singleNumberIII(self, A):
    # write your code here
    a = []
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A) - 1):
            if (A[i] == A[j]):
                break
        else:
            a.append(A[i])

        if ((len(a)) == 2):
            return a