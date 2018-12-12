class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        for i in range(0, len(nums) - 1):
            if (nums[i] == target):
                return i

        return -1