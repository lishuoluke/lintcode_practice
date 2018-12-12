class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, nums):
        # write your code here
        product = 1
        product1 = 1
        list = []
        if (len(nums) == 1 and nums[0] == 0):
            list.append(1)
            return list

        if (nums.count(0) >= 2):
            for itemss in nums:
                list.append(0)
            return list

        for item in nums:
            product = product * item
            if (item != 0):
                product1 = product1 * item

        for items in nums:
            if (items != 0):
                list.append(int(product / items))
            else:
                list.append(product1)

        return list
