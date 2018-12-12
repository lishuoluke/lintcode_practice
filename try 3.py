COUNT = 0
llist = []

def perm(list,n, begin, end):
    global COUNT

    if begin >= end:
        list.append (n)
    else:
        i = begin
        for num in range(begin, end):
            n[num], n[i] = n[i], n[num]
            #llist.append(n)
            perm(n, begin + 1, end)
            n[num], n[i] = n[i], n[num]

n = [1, 2, 3, 4]
perm(n, 0, len(n))
print (COUNT)
#print (llist)