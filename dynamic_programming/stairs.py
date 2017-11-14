class Solution:
    # @param A : integer
    # @return an integer

    def __init__(self):
        self.count = 0
        self.save = None

    def climbStairs(self, A):
        self.save = [-10] * (A+3)
        x = self.stairs(0, A)
        # print self.save
        return x


    def stairs(self, current, final):
        if current == final:
            return 1

        if current > final:
            return self.count

        if self.save[current] != -10:
            return self.save[current]

        self.save[current] = self.stairs(current+1, final) + self.stairs(current+2, final)
        return self.save[current]


print Solution().climbStairs(3)




