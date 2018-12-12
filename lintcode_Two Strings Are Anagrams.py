class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    def anagram(self, s, t):
        # write your code here
        aaa = list(s)
        bbb = list(t)
        for item in aaa:
            if (aaa.count(item) != bbb.count(item)):
                return False

        return True
