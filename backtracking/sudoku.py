class Solution:
    # @param A : list of list of chars
    # @return nothing
    def __init__(self):
        self.A = None

    def solveSudoku(self, A):

        A = [list(a[0]) for a in A]
        i = 0

        changes = []

        while i < len(A):
            j = 0
            while j < len(A[0]):
                if A[i][j] == '.':
                    A[i][j] = 0
                    changes.append((i, j))
                else:
                    A[i][j] = int(A[i][j])

                j += 1

            i += 1

        self.A = A

        A[0][2] = 4
        print self.check_possible((0, 2))

        self.sudoku(changes)

        return self.A

    def get_block(self, c):
        (i, j) = c
        blocks_cor = [2, 5, 8]

        ti = 0
        tj = 0

        for m in blocks_cor:
            if i <= m:
                ti = m
                break
        for m in blocks_cor:
            if j <= m:
                tj = m
                break

        block = []
        li = ti
        while li > ti-3:
            lj = tj
            while lj > tj-3:
                block.append(self.A[li][lj])
                lj -= 1
            li -= 1
        return block

    def check_possible(self, c):

        i, j = c
        check = self.A[i][j]

        row = self.A[i]
        col = [self.A[x][j] for x in xrange(len(self.A))]

        block = self.get_block(c)

        count = 0

        for i in xrange(9):
            if check == row[i]:
                count += 1

            if check == col[i]:
                count += 1

            if check == block[i]:
                count += 1

        if count == 3:
            return True
        else:
            return False

    def sudoku(self, changes):

        (i, j) = changes[0]

        for d in xrange(1, 10):
            self.A[i][j] = d
            if self.check_possible((i, j)):
                self.sudoku(changes[1:])
        else:
            return


A = [['53..7....'], ['6..195...'], ['.98....6.'], ['8...6...3'], ['4..8.3..1'], ['7...2...6'], ['.6....28.'], ['...419..5'], ['....8..79']]
print Solution().solveSudoku(A)




