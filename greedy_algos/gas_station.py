class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):

        if len(gas) <= 1:
            return 0

        l = len(gas)

        g = 0
        while g < len(gas):

            init = g
            nxt = g
            first = True
            car = 0
            broke = False
            while not nxt == init or first:
                if first:
                    car = gas[init]
                    car -= cost[init]
                    first = False
                else:
                    car += gas[nxt]
                    car -= cost[nxt]

                if car >= 0:
                    nxt += 1
                    nxt = nxt % l
                else:
                    broke = True
                    break

            if not broke:
                return init

            g += 1

        return -1

A = [1, 2]
B = [2, 1]
print Solution().canCompleteCircuit(A, B)