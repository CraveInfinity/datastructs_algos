# naive approach 1 --- did not work if the given array B has duplicates
#
# class Solution:
#     # @param A : string
#     # @param B : tuple of strings
#     # @return a list of integers
#     def findSubstring(self, A, B):
#
#         if len(A) == 0:
#             return []
#
#
#         def common_elements(arr):
#             result = set(arr[0])
#             for currSet in arr[1:]:
#                 result.intersection_update(currSet)
#
#             return list(result)
#
#         l = len(B)
#         ll = len(B[0])
#
#
#         i = 0
#
#         while i + (l * ll) <= len(A):
#             m = A[i: i + (l * ll)]
#
#             # print m
#
#             j = 0
#             while j + ll <= len(m):
#                 n = m[j:j + ll]
#
#                 if d.has_key(n):
#                     d[n].append(i)
#
#                 j += ll
#                 # print n
#             i += 1
#
#
#         return common_elements(d.values())


""" Approach 2: ord the array B and the m"""


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):

        def hash_func(x):
            k = 0
            for i in x:
                k += hash(i)
            return k


        if len(A) == 0:
            return []

        l = len(B)
        ll = len(B[0])

        bl = hash_func(B)


        i = 0
        res = []
        while i + (l * ll) <= len(A):
            m = A[i: i + (l * ll)]

            y = []

            j = 0
            while j + ll <= len(m):
                n = m[j:j + ll]
                j += ll
                y.append(n)

            if hash_func(y) == bl:
                res.append(i)

            i += 1

        return res






""" weaker solution approach in editorial 

--- original thought out approach in the solution editorial

 -- takes O(n * nlogn) time
      -- iter through String A, with total concatenated B length
      -- if first word length substring found
      -- check the rest of the word substring in A if exists in B and remove if exists
      -- if array is empty the substring matches appedn in the final return list else increment i to move through string"""

A = "barfoothefoobarman"
B = ["foo", "bar"]

# A = "aaacabbbcccccacacbbac"
# B = ["aa", "ac", "ac", "bb", "bb", "ac", "bb"]
print Solution().findSubstring(A, B)