class Solution:
    """
    @param nums: the num arrays
    @return: the num arrays after rearranging
    """

    def rearrange(self, nums):
        # Write your code here
        llist = [None] * len(nums)

        nums.sort()
        print(nums)
        if len(nums) % 2 == 0:
            count = 0
            hello = 0
            while count < len(nums):
                llist[count] = nums[hello]
                llist[count + 1] = nums[int(len(nums) / 2 + count / 2)]
                hello = hello + 1
                count = count + 2

        if len(nums) % 2 == 1:
            count = 0
            hello = 0
            while count < len(nums) - 1:
                llist[count] = nums[hello]
                llist[count + 1] = nums[int((len(nums) + 1) / 2) + hello]
                count = count + 2
                hello = hello + 1
            llist[-1] = nums[int((len(nums) - 1) / 2)]

        return llist
