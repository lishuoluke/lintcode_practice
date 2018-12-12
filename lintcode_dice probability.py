##扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        if n == 0: return None
        result = [
            [1, 1, 1, 1, 1, 1],
        ]
        # if n == 1: return result[0]
        # 计算n个骰子出现的各个次数和
        for i in range(1, n):
            x = 5 * (i + 1) + 1
            result.append([0 for _ in range(x)])
        # Create the specific entries for the row
            for j in range(x):
                if j < 6:
                    result[i][j] = (sum(result[i - 1][0:j + 1]))
                elif 6 <= j <= 3 * i + 2:
                    result[i][j] = (sum(result[i - 1][j - 5:j + 1]))
                else:
                    break
            left = 0
            right = len(result[i]) - 1
            while left <= right:
                result[i][right] = result[i][left]
                left += 1
                right -= 1
        # Take value of last line of array
        res = result[-1]

        all = float(sum(res))
        other = []
        # 第i个元素代表骰子总和为n+i
        for i, item in enumerate(res):
            # pro = self.round(item/all)
            # 自己写的四舍五入算法和LintCode有出入，其实网站自身会处理数据，这里不再做处理
            pro = item / all
            other.append([n + i, pro])
        return other

    def round(self, num):
        # 将概率值四舍五入
        num = num * 100
        num = int(2 * num) / 2 + int(2 * num) % 2
        num = num / 100.0
        return num

#n=1　　:　　[1, 1, 1, 1, 1, 1]
#n=2　　:　　[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
#n=3　　:　　[1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1]
#n=4　　:　　[1, 4, 10, 20, 35, 56, 80, 104, 125, 140, 146, 140, 125, 104, 80, 56, 35, 20, 10, 4, 1]
#n=5　　:　　[1, 5, 15, 35, 70, 126, 205, 305, 420, 540, 651, 735, 780, 780, 735, 651, 540, 420, 305, 205, 126, 70, 35, 15, 5, 1]
#n=6　　:　　[1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, 3431, 3906, 4221, 4332, 4221, 3906, 3431, 2856, 2247, 1666, 1161, 756, 456, 252, 126, 56, 21, 6, 1]

#just copy half, the other half is mirror reflection
# if <6 , add all before, >6, add 6 before

    array_test= dicesSum(5,1)
    print(array_test)