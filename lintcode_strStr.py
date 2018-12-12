def strStr(self, source, target):
    # write your code here
    if (source is None or target is None):
        return -1
    if (target == ''):
        return 0
    if (target == source):
        return 0
    aaa = list(source)
    bbb = list(target)

    if (len(aaa) < len(bbb)):
        return -1
    for i in range(0, len(aaa) - len(bbb) + 1):
        for j in range(0, len(bbb)):
            haha = aaa[i + j]
            hehe = bbb[j]
            if (aaa[i + j] == bbb[j]):
                if (j == len(bbb) - 1):
                    return i
                continue
            else:
                break
    return -1

print (strStr(1,"abcde", "e"))