MOD = 10000003


class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        A = list(A)

        i = 0
        x_list = []
        while i < len(A):
            if A[i] == 'x':
                x_list.append(i)
            i += 1

        print A
        print x_list

        if len(x_list) < 2:
            return 0

        median = sum(x_list) / len(x_list)

        i = 0
        while i < len(x_list):
            if i > 0:
                if m_diff > abs(median - x_list[i]):
                    m_diff = abs(median - x_list[i])
                    mi = i
            else:
                m_diff = abs(median - x_list[i])
                mi = i

            i += 1

        print m_diff
        print x_list[mi]

        A[x_list[mi]] = '.'

        x_list.remove(x_list[mi])
        count = m_diff

        print x_list
        print count


        def count_x(arr):
            print arr
            c = 0
            for i in arr:
                if i == 'x':
                    c += 1
            return c

        i = 0
        while i < len(x_list):
            if median > x_list[i]:
                # print abs(x_list[i] - median) - 1 - count_x(A[x_list[i]+1:median])
                count += abs(x_list[i] - median) - 1 - count_x(A[x_list[i]+1:median])
            else:
                # print count_x(A[median+1:x_list[i]])
                # print abs(x_list[i] - median) - 1 - count_x(A[median+1:x_list[i]])
                count += abs(x_list[i] - median)-1 - count_x(A[median+1:x_list[i]])
            i += 1
            print ''

        return count % MOD


A = "....x..xx...x.."
A = ".x.x.x..x"
A = "x.x.xx.x.xxx.......x..x.xxx..x.xxx"

print Solution().seats(A)