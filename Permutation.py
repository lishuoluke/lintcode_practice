#a = list(range(4))
a=[1,2,3,4]
print (a)
print ('*********')
def go(beg):

    if beg >= len(a):
        print(a)
    for i in range(beg, len(a)):
        a[beg], a[i] = a[i], a[beg] #exchange value
        go(beg + 1)
        a[beg], a[i] = a[i], a[beg]#exchange value

go(0)
