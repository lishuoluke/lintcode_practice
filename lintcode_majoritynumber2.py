class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        if (len(nums)==1):
            return nums[0]
        for item in nums:
            if (nums.count(item) > len(nums)/3):
                return item