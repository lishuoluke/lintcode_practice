class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        primes = [2, 3, 5]
        nums = [0] * n
        nums[0] = 1
        primesIndex = [0] * len(primes)
        count = 1
        while (count < n):
            mini = 99999999999999
            for i in range(0, len(primes)):
                # 求乘以每一个因子得到的最小丑数
                temp = nums[primesIndex[i]] * primes[i];
                mini = min(temp, mini)

            for i in range(0, len(primes)):
                # 更新index，可能更新多个index
                if (mini == nums[primesIndex[i]] * primes[i]):
                    primesIndex[i] = primesIndex[i] + 1
            nums[count] = mini
            count = count + 1

        return nums[count - 1]