def maxSubArray(self, nums):
    # write your code here
    currentmax = -100000
    currentend = 0
    if (len(nums) == 1):
        return nums[0]
    for i in range(0, len(nums)):
        if (currentend < 0):
            currentend = 0
        currentend = currentend + nums[i]
        currentmax = max(currentmax, currentend)

    return currentmax

print (maxSubArray(1,[-1]))