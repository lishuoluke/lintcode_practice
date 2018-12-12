class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here

        # write your code here
        currentmin = 300000000
        currentend = 0
        if (len(nums) == 1):
            return nums[0]
        for item in nums:
            if (currentend > 0):
                currentend = 0
            currentend = currentend + item
            currentmin = min(currentmin, currentend)

        return currentmin