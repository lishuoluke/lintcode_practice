class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        # write your code here
        max = -1
        list = []
        for item in dictionary:
            if len(item) > max:
                max = len(item)
        for haha in dictionary:
            if len(haha) == max:
                list.append(haha)

        return list
