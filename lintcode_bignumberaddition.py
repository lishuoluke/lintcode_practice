class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """

    def addStrings(self, num1, num2):
        # write your code here
        # write your code here
        aaa = list(num1)
        bbb = list(num2)
        aaa.reverse()
        bbb.reverse()

        if (len(aaa) > len(bbb)):
            for i in range(0, len(aaa) - len(bbb)):
                bbb.append(0)

        if (len(bbb) > len(aaa)):
            for i in range(0, len(bbb) - len(aaa)):
                aaa.append(0)

        length = max(len(aaa), len(bbb)) + 1
        ccc = [0 for k in range(0, length)]
        carryforward = 0
        for i in range(0, len(aaa)):
            sum = int(aaa[i]) + int(bbb[i]) + carryforward
            if (sum < 10):
                ccc[i] = sum
                carryforward = 0
            else:
                ccc[i] = sum - 10
                carryforward = 1
        ccc[len(ccc) - 1] = carryforward

        ccc.reverse()
        while (len(ccc) > 1 and ccc[0] == 0):
            del ccc[0]
        result = ''
        for n in range(0, len(ccc)):
            result = result + str(ccc[n])

        return result
