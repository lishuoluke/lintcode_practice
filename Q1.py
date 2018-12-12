#题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

number = int (input())
remainder = 2
start = 9
while (remainder != 0):
    remainder = start % number
    if (remainder == 0):
        length = len (str(start))
        break
    start = start * 10 + 9

print (str(length) + ' 9 is divisible by '+ str(number))
print (str(start) + ' / ' + str(number) + ' = ' + str(start/number))