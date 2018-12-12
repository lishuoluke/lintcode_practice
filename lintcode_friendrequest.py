class Solution:
    """
    @param ages: The ages
    @return: The answer
    """

    def friendRequest(self, ages):
        # Write your code here

        count = 0
        for i in range(0, len(ages) - 1):
            for j in range(i + 1, len(ages)):
                if not (ages[i] <= 0.5 * ages[j] + 7 or ages[i] > ages[j] or (ages[i] < 100 and ages[j] > 100)):
                    count = count + 1
                if not (ages[j] <= 0.5 * ages[i] + 7 or ages[j] > ages[i] or (ages[j] < 100 and ages[i] > 100)):
                    count = count + 1
        return count