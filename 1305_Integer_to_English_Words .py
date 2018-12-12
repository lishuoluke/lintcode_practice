class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """

    def numberToWords(self, num):
        # Write your code here

        def three_digit(number):

            List_number = list(number)
            string = ''
            leadningones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
            tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                     'Nineteen']
            trailingones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
            if List_number[0] == '0':
                string = string
            else:
                index = int(List_number[0])
                string = string + leadningones[index] + ' Hundred '

            if List_number[1] == '1':
                index = int(List_number[2])
                string = string + teens[index]
                return string

            else:
                index1 = int(List_number[1])
                index2 = int(List_number[2])
                string = string + tens[index1] + ' ' + trailingones[index2]
                return string.strip()

        if num == 0:
            return 'Zero'
        string = str(num)
        length = len(string)
        unitss = ['', 'Thousand', 'Million', 'Billion']
        remainder = length % 3
        words = ''
        if remainder == 1:
            string = '00' + string
        if remainder == 2:
            string = '0' + string
        new_length = len(string)
        loop = int(new_length / 3)
        for i in range(0, loop):
            words = words + three_digit(string[3 * i:3 + 3 * i]) + ' ' + unitss[loop - 1 - i] + ' '
        words.strip()
        return ' '.join(words.split())