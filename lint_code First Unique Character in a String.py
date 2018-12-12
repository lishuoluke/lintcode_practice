class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        aaa = list(str)
        aaa.sort()
        for i in range(0, len(aaa)):
            if i == 0:
                if aaa[0] != aaa[1]:
                    return aaa[0]
            elif (i == len(aaa) - 1):
                if aaa[i] != aaa[i - 1]:
                    return aaa[i]

            else:
                if (aaa[i] != aaa[i + 1] and aaa[i] != aaa[i - 1]):
                    return aaa[i]