class MinStack:
    def __init__(self):
        self.items = []
        self.m = []

    # @param x, an integer
    def push(self, x):
        self.items.append(x)




    # @return nothing
    def pop(self):
        if self.items:
            self.items.pop()

    # @return an integer
    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        pass




