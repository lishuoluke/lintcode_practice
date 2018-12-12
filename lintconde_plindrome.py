#Palindrome Number II : convert the number into binary then check whether the binary is a palindrome or not


def isPalindrome(self, n):
    # Write your code here
    if (n == 0 or n == 1):
        return True
    number = "{0:b}".format(n)
    #print (number)
    if (number == 0 or number == 1):
        return True
    stringer = str(number)
    listee = list(stringer)
    length = int(len(listee) / 2)
    for i in range(0, length + 1):
        number1 = listee[i]
        number2 = listee[len(listee)- 1 - i]
        if (number1 != number2):
              return False
        else:
            if (i != length - 1):
                continue
            else:
                return True




print (isPalindrome(1,14))