class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        sum = []
        if nums == []:
            return []
        sum_1 = 0
        for j in range(0, k):
            sum_1 = sum_1 + nums[j]
        sum.append(sum_1)
        for i in range(1, len(nums) - k + 1):
            sum_1 = sum_1 - nums[i - 1]
            sum_1 = sum_1 + nums[i + k - 1]
            sum.append(sum_1)

        return sum

