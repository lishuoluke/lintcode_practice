class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """

    def getStream(self, s):
        # Write your code here
        checklist = []
        for i in range(0, len(s) - 1):
            for j in range(0, int(i / 2) + 1):
                if (s[j] != s[i - j]):
                    checklist.append(0)
                    break
                elif (j == int(i / 2)):
                    checklist.append(1)

        return checklist

# the checking in the website is wrong, this code is correct, validate using string fdfeceedaaddaf