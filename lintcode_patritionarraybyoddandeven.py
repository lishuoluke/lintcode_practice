class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        llist = []
        l = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

        return nums
