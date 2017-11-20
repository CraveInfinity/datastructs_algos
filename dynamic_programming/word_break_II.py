class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):

        if not A or not B:
            return []

        self.A = A
        self.word_dict = B
        self.final_strings = []
        self.word_split([], A)
        x = [' '.join(z) for z in sorted(self.final_strings)]

        return x

    def word_split(self, splited, string):
        if ''.join(splited) == self.A:
            self.final_strings.append(splited)
            return

        for i in xrange(len(string)+1):
            substr = string[:i]
            if substr in self.word_dict:
                self.word_split([s for s in splited] + [substr], string[i:])




A = 'catsanddog'
B = ["cat", "cats", "and", "sand", "dog"]

A = "aabbbabaaabbbabaabaab"
B = [ "bababbbb", "bbbabaa", "abbb", "a", "aabbaab", "b", "babaabbbb", "aa", "bb" ]

print Solution().wordBreak(A, B)


