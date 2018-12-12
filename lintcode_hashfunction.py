class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here

        aa = list(key)
        aa.reverse()
        value = ord(aa[0])

        # key10 =  map(ord,key)
        base = 1
        for i in range(1, len(key)):
            number = ord(aa[i])
            value = value + (33 * base * number)
            base = base * 33 % HASH_SIZE
        value = value % HASH_SIZE
        return value