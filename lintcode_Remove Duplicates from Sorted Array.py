class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        n = 0
        while (n < len(nums) - 1):
            if (nums[n] < nums[n + 1]):
                n = n + 1
                continue
            else:
                del nums[n]

        return