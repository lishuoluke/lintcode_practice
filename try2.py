def permute(self, nums):
    # write your code here
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []

    def helper(res, l, r, n, max):
        if n == max:
            res.append(l)
        for i in range(0, len(r)):
            helper(res, l + [r[i]], r[:i] + r[i + 1:], n + 1, max) # r[:i] + r[i + 1:],all in the list except for list[i]

    helper(res, [], nums, 0, len(nums))
    return res


haa = permute(1,[1,2,3,4])
print(haa)