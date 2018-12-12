class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        if (len(nums) == 1):
            return nums[0]
        for i in range(0, len(nums) - 1):

            if (nums.count(nums[i]) > len(nums) / 2):
                return nums[i]