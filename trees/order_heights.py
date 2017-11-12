class Solution(object):
    # @param heights : list of integers
    # @param infronts : list of integers
    # @return a list of integers

    def __init__(self):
        self.pos_idx = None
        self.h = None
        self.position = None

    def order(self, heights, infronts):

        h_dict = {k: v for k, v in zip(heights, infronts)}
        print h_dict
        print

        self.h = [-1] * len(h_dict)

        for idx, k in enumerate(sorted(h_dict.keys())):
            print self.h
            self.position = h_dict[k]

            self.build_segment_tree(0, len(self.h))

            self.h[self.pos_idx] = k

        return self.h

    def f(self, start, end):
        k = self.h[start:end]
        print k

        count = 0
        for i in k:
            if i == -1:
                count += 1

        return count

    def build_segment_tree(self, start, end):
        if start == end:
            self.pos_idx = end
            return

        mid = start + (end - start) / 2
        empty_spaces = self.f(start, end)

        print empty_spaces

        if empty_spaces == self.position:
            self.pos_idx = end
            return
        elif empty_spaces >= self.position:
            print 'left'
            self.build_segment_tree(start, mid)
        else:
            print 'right'
            self.position = empty_spaces
            self.build_segment_tree(mid+1, end)


A = [ 86, 77 ]
B = [ 0, 1 ]


A = [ 86, 92, 49, 21, 62, 27, 90, 59 ]
B = [ 2, 0, 0, 2, 0, 2, 1, 3 ]

print Solution().order(A, B)