class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        nums.sort()
        total = len(nums)
        if (total%2 == 0):
            return nums[total/2-1]
        else:
            return nums[(total-1)/2]