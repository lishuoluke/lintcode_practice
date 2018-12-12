class Solution:
    """
    @param str: The input string
    @return: The answer
    """

    def dataSegmentation(self, str):
        # Write your code here
        newlist = []
        aa = list(str)
        current = ''
        for item in aa:
            if item.isalpha() == True:
                current = current + item

            else:
                if (current != ''):
                    newlist.append(current)
                if (item != ' '):
                    newlist.append(item)
                current = ''
        if (current != ''):
            newlist.append(current)
        return newlist
