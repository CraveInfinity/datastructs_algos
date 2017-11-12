class Solution:
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers
    def order(self, heights, infronts):

        h_dict = {k: v for k, v in zip(heights, infronts)}

        # print sorted(h_dict.keys())

        h = [-1] * len(h_dict)

        for idx, k in enumerate(sorted(h_dict.keys())):
            # print h
            count = 0
            ix = 0
            while ix < len(h):
                if count == h_dict[k] and h[ix] == -1:
                    # print ix
                    h[ix] = k
                    break
                if h[ix] == -1:
                    count += 1

                ix += 1

        return h


A = [ 86, 77 ]
B = [ 0, 1 ]


A = [ 86, 92, 49, 21, 62, 27, 90, 59 ]
B = [ 2, 0, 0, 2, 0, 2, 1, 3 ]

print Solution().order(A, B)