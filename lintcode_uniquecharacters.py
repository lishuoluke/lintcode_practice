class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        # write your code here
        aaa = list(str)
        for item in aaa:
            if aaa.count(item) > 1:
                return False

        return True
