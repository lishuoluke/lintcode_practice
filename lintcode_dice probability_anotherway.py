##扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        total = 6 ** n
        dice_pol = [1] * 6
        output_pol = [1]

        for i in range(0, n):
            output_pol = poly_multiply(output_pol, dice_pol)

        output = []
        for dice in range(n, 6 * n + 1):
            output.append([dice, output_pol[dice - n] / total])

        return output


def poly_multiply(pol1, pol2):
    n1 = len(pol1)
    n2 = len(pol2)
    outlengh = n1 + n2 - 1

    output = [0] * outlengh

    for i in range(0, outlengh):
        sum = 0
        for k in range(0, i + 1):
            if (k < n1 and (i - k) < n2):
                sum += pol1[k] * pol2[i - k]
        output[i] = sum
    return output
