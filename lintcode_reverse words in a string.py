class Solution:
    """
    @param: s: A string
    @return: A string
    """

    def reverseWords(self, s):
        # write your code here
        B = s.split()
        B.reverse()
        result = ''
        for item in B:
            result = result + item + ' '

        return result        