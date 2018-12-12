class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        sum = 0
        carry = 0
        for i in range(32):
            a1 = a & 1
            b1 = b & 1
            val = 0
            if a1== 0 and b1 ==0 and carry ==0:
                val =0
                carry = 0
            elif a1 == 1 and b1 == 1 and carry ==1:
                val =1
                carry =1
            elif a1 == 0 and b1 ==0 or a1==0 and carry ==0 or b1 ==0 and carry ==0:
                val = 1
                carry = 0
            else:
                val = 0
                carry = 1
            val = val << i
            sum = sum|val
            a = a>>1
            b = b>>1
        return sum


print(Solution.aplusb(1,2,3))