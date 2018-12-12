
    # @param {integer[]} nums
    # @return {integer[][]}
def subsets(nums):
        if nums is None:
            return []

        result = []
        nums.sort()
        dfs(nums, 0, [], result)
        return result

def dfs(nums, pos, list_temp, ret):
        # append new object with []
    ret.append([] + list_temp)

    for i in range(pos, len(nums)):
        list_temp.append(nums[i])
        dfs(nums, i + 1, list_temp, ret)
        list_temp.pop()

A=[1,2,3]

B = subsets(A)
print (B)
