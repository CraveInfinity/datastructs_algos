# Definition for singly-linked list.


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        def getlength(x):
            l = 0
            while not x.next == None:
                l += 1
                x = x.next

            return l

        m = getlength(A)
        n = getlength(B)

        d = n - m

        if m > n:
            t = A
            A = B
            B = t
            d = n - m

        i = 0
        while i < d:
            B = B.next
            i += 1

        while not A.next == None and not B.next == None:
            if A == B:
                return A

            A = A.next
            B = B.next

        return None



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

d = ListNode(3)
d.next = None
c = ListNode(2)
c.next = d
b = ListNode(5)
b.next = c
B = ListNode(1)
B.next = b

A = b


print Solution().getIntersectionNode(A, B).val