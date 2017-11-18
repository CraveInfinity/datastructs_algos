class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        return self.edit_distance(A, 0, B, 0)

    def edit_distance(self, A, index_a, B, index_b):

        if index_a == len(A) and not index_b == len(B):
            return 1
        if not index_a == len(A) and index_b == len(B):
            return 1

        if index_a == len(A) and index_b == len(B):
            return 0

        if A[index_a] == B[index_b]:
            return self.edit_distance(A, index_a+1, B, index_b+1)
        else:
            return min(
                1 + self.edit_distance(A, index_a + 1, B, index_b),
                1 + self.edit_distance(A, index_a, B, index_b + 1),
                1 + self.edit_distance(A, index_a + 1, B, index_b + 1)
            )





A = 'Anshumanxxx'
B = 'Antihuman'

print Solution().minDistance(A, B)