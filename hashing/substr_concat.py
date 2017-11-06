class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):

        if len(A) == 0:
            return []


        def common_elements(arr):
            result = set(arr[0])
            for currSet in arr[1:]:
                result.intersection_update(currSet)

            return list(result)

        l = len(B)
        ll = len(B[0])

        d = {'{}_{}'.format(k, i): [] for i, k in enumerate(B)}

        i = 0

        while i + (l * ll) <= len(A):
            m = A[i: i + (l * ll)]

            # print m

            j = 0
            while j + ll <= len(m):
                n = m[j:j + ll]

                if d.has_key(n):
                    d[n].append(i)

                j += ll
                # print n
            i += 1


        return common_elements(d.values())


A = "barfoothefoobarman"
B = ["foo", "bar"]

A = "aaacabbbcccccacacbbac"
B = [ "aa", "ac", "ac", "bb", "bb", "bb", "ac" ]
print Solution().findSubstring(A, B)