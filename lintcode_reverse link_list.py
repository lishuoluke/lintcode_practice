class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        p = head
        list = []
        while (p):
            list.insert(0, p.val)
            p = p.next

        p = head
        for item in list:
            p.val = item
            p = p.next

        return head