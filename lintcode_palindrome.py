class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
            aaa  = list(str(num))
            for i in range (0,len(aaa)):
                if aaa[i] != aaa[len(aaa)-1-i]:
                    return False
            return True