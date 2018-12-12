class MinStack:
    def __init__(self):
        # do intialization if necessary

        self.stack1 = []
        self.stack2 = []

    def push(self, number):
        # write your code here
        self.stack1.append(number)
        if len(self.stack2) == 0 or number <= self.stack2[-1]:
            self.stack2.append(number)

    def pop(self):
        # write your code here

        tmp = self.stack1.pop()

        if tmp == self.stack2[-1]:
            return self.stack2.pop()
        else:
            return tmp

    def min(self):
        # write your code here
        return self.stack2[-1]
