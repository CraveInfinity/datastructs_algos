class Solution:
    # @param A : list of list of chars
    # @return nothing
    def __init__(self):
        self.A = A

    def solveSudoku(self, A):

        A = [list(a) for a in A]

        for x in xrange(9):
            for y in xrange(9):
                if not A[x][y] == '.':
                    A[x][y] = int(A[x][y])
                else:
                    A[x][y] = 0

        self.sudoku(A, i=0, j=0)

        for x in xrange(9):
            for y in xrange(9):
                A[x][y] = str(A[x][y])
            A[x] = ''.join(A[x])

        self.A = A

        # A = [''.join(str(p) for p in q) for q in A]

    # def get_block(self, c):
    #     (i, j) = c
    #     blocks_cor = [2, 5, 8]
    #
    #     ti = 0
    #     tj = 0
    #
    #     for m in blocks_cor:
    #         if i <= m:
    #             ti = m
    #             break
    #     for m in blocks_cor:
    #         if j <= m:
    #             tj = m
    #             break
    #
    #     block = []
    #     li = ti
    #     while li > ti-3:
    #         lj = tj
    #         while lj > tj-3:
    #             block.append(self.grid[li][lj])
    #             lj -= 1
    #         li -= 1
    #     return block

    # def check_possible(self, c):
    #
    #     i, j = c
    #     check = self.A[i][j]
    #
    #     row = self.A[i]
    #     col = [self.A[x][j] for x in xrange(len(self.A))]
    #
    #     block = self.get_block(c)
    #
    #     count = 0
    #
    #     for i in xrange(9):
    #         if check == row[i]:
    #             count += 1
    #
    #         if check == col[i]:
    #             count += 1
    #
    #         if check == block[i]:
    #             count += 1
    #
    #     if count == 3:
    #         return True
    #     else:
    #         return False

    @staticmethod
    def getnextNumber(grid, i, j):

        for l in xrange(i, 9):
            for m in xrange(j, 9):
                if grid[l][m] == 0:
                    return l, m

        for l in xrange(0, 9):
            for m in xrange(0, 9):
                if grid[l][m] == 0:
                    return l, m

        return -1, -1

    @staticmethod
    def is_valid(grid, i, j, e):
        row_ok = all([e != grid[i][x] for x in range(9)])
        if row_ok:
            column_ok = all([e != grid[x][j] for x in range(9)])
            if column_ok:
                # finding the top left x,y co-ordinates of the section containing the i,j cell
                sec_top_x, sec_top_y = 3 *(i/3), 3 *(j/3)
                for x in range(sec_top_x, sec_top_x+3):
                    for y in range(sec_top_y, sec_top_y+3):
                        if grid[x][y] == e:
                            return False
                return True
        return False

    def sudoku(self, grid, i, j):

        i, j = self.getnextNumber(grid, i, j)
        if i == -1:
            return True

        # for d in xrange(1, 10):

            # if self.check_possible((i, j)):
            #     self.A[i][j] = d
            #     if self.sudoku(i, j):
            #         return True
            #     self.A[i][j] = 0

        for d in xrange(1, 10):
            if self.is_valid(grid, i, j, d):
                grid[i][j] = d
                if self.sudoku(grid, i, j):
                    return True
                grid[i][j] = 0

        return False


A = [ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]

k = Solution()
print k.solveSudoku(A)

print k.A




