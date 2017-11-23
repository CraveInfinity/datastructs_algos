# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @param D : integer
#     # @param E : list of integers
#     # @param F : list of integers
#     # @return a strings
#
#     def __init__(self):
#         self.found = None
#         self.A = None
#         self.B = None
#         self.rect = None
#         self.radius = None
#         self.circles = None
#
#     def solve(self, A, B, C, D, E, F):
#         self.A = A
#         self.B = B
#
#         self.rect = [[1]*(B+1)]*(A+1)
#         # print self.rect
#
#         self.radius = D
#         self.circles = C
#
#         for c in xrange(self.circles):
#             cx = E[c]
#             cy = F[c]
#
#             for i in xrange(A+1):
#                 for j in xrange(B+1):
#                     dist = self.distance((i, j), (cx, cy))
#                     if dist <= float(self.radius):
#                         self.rect[i][j] = 0
#
#         # print self.rect
#
#         self.found = False
#         self.reach_rect(0, 0)
#
#         if self.found:
#             return 'YES'
#         else:
#             return 'NO'
#
#     def isvalid(self, x, y):
#         if self.A >= x >= 0 and self.B >= y >= 0:
#             if self.rect[x][y]:
#
#                 return True
#
#         return False
#
#     def reach_rect(self, x, y):
#         if x > self.A or y > self.B:
#             return 0
#
#         if x == self.A and y == self.B:
#             self.found = True
#             return 0
#         if not self.found:
#             for i in xrange(2):
#                 for j in xrange(2):
#                     if i == 0 and j == 0:
#                         pass
#                     else:
#                         xi = x + i
#                         yi = y + j
#
#                         if self.isvalid(xi, yi):
#                             self.reach_rect(xi, yi)
#
#     @staticmethod
#     def distance(a, b):
#         m = a[1] - b[1]
#         n = a[0] - b[0]
#         d = (m**2 + n**2)**0.5
#         return d




class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings

    def __init__(self):
        self.found = None
        self.A = None
        self.B = None
        self.E = None
        self.F = None
        self.radius = None
        self.circles = None

    def isvalid(self, x, y):
        if self.A >= x >= 0 and self.B >= y >= 0:
            if self.is_distant(x, y):
                return True

        return False

    def solve(self, A, B, C, D, E, F):
        self.A = A
        self.B = B

        self.E = E
        self.F = F

        self.radius = D
        self.circles = C

        q = Queue()
        q.enqueue((0, 0))

        while not q.isEmpty():
            current = q.front()
            q.dequeue()

            if current[0] == self.A and current[1] == self.B:
                return 'YES'
            for i in xrange(2):
                for j in xrange(2):

                    if i == 0 and j == 0:
                        pass
                    else:
                        nexti = current[0] + i
                        nextj = current[1] + j
                        if self.isvalid(nexti, nextj):
                            if current[0] == self.A and current[1] == self.B:
                                return 'YES'
                            q.enqueue((nexti, nextj))

        return 'NO'

    def is_distant(self, x, y):

        for c in xrange(self.circles):
            cx = self.E[c]
            cy = self.F[c]

            m = cx - x
            n = cy - y
            d = (m ** 2 + n ** 2) ** 0.5

            if d > self.radius:
                pass
            else:
                return False

        return True


print Solution().solve(10, 10, 1, 1, [10], [10])