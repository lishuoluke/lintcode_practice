
#写一个程序来找第 n 个超级丑数。

#超级丑数的定义是正整数并且所有的质数因子都在所给定的一个大小为 k 的质数集合内。

#比如给你 4 个质数的集合 [2, 7, 13, 19], 那么 [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] 是前 12 个超级丑数。

#样例
#给出 n = 6 和质数集合 [2, 7, 13, 19]。第 6 个超级丑数为 13，所以返回 13 作为结果

#declare the answer array
import sys


"""
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """
import sys
def nthSuperUglyNumber(self, n, primes):

    # write your code here
    nums = [0] * n
    nums[0] = 1
    primesIndex = [0] * len(primes)
    count = 1
    while (count < n):
        mini = 999999
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


number = nthSuperUglyNumber(1,8,[2,5,7,31])
print (number)




