def rotateString(self, str, offset):
    # write your code here
    aaa = list(str)
    result = ''
    for i in range(0, len(aaa)):
        index = (i + offset + 1) % len(aaa)
        result = result + aaa[index]
    return result
print (rotateString(1,'abcdefg',3))