class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return product of num1 and num2
    """

    def multiply(self, num1, num2):
        # write your code here
        aaa = list(num1)
        bbb = list(num2)
        aaa.reverse()
        bbb.reverse()
        ccc = [0 for k in range(0, len(aaa) + len(bbb))]
        for i in range(0, len(aaa)):
            for j in range(0, len(bbb)):
                ccc[i + j] += int(aaa[i]) * int(bbb[j]) #accumulate the sum of [i][j] and [j][i]

        for m in range(0, len(ccc)):
            if (ccc[m] > 9):
                ccc[m + 1] += ccc[m] // 10
                ccc[m] = ccc[m] % 10

        ccc.reverse()
        while (len(ccc) > 1 and ccc[0] == 0):
            del ccc[0]
        result = ''
        for n in range(0, len(ccc)):
            result = result + str(ccc[n])

        return result


print ( Solution.multiply(8,'000011','011') )