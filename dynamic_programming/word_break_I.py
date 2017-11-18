""" Close to possible approach """

# _end_ = '_end_'
#
#
# class Solution(object):
#     # @param A : string
#     # @param B : list of strings
#     # @return an integer
#     def wordBreak(self, A, B):
#         if len(A) == 0:
#             return 0
#         if len(B) == 0:
#             return 0
#         trie = self.get_trie(B)
#         print trie['b']['_end_']
#
#         print trie
#
#         root = trie
#         l = []
#         x = []
#         for i, letter in enumerate(A):
#             if letter in root:
#                 root = root[letter]
#                 l.append(letter)
#                 if _end_ in root:
#                     if i+1 < len(A) and A[i+1] in root:
#                         pass
#                     else:
#                         x.extend(l)
#                         l = []
#                         root = trie
#
#         print ''.join(x)
#         print x
#         print A
#
#         if ''.join(x) == A:
#             return 1
#         else:
#             return 0
#
#     @staticmethod
#     def get_trie(words):
#         root = {}
#
#         for word in words:
#             current_dict = root
#             for letter in word:
#                 current_dict = current_dict.setdefault(letter, {})
#
#             current_dict[_end_] = _end_
#
#         return root


""" Solution  Approach """


class Solution(object):
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        self.B = B
        self.dp = [[-1]*len(A)]*len(A)
        self.trie = self.get_trie(B)
        return self.words(0, A)

    def words(self, index, string):
        if index == len(string):
            return True
        result = False
        i = index

        # while i < len(string):
        #     if self.dp[index][i] != -1:
        #          result = self.dp[index][i]
        #     else:
        #         sub_str = string[index:i+1]
        #         if self.search_trie(sub_str):
        #             result |= self.words(i+1, string)
        #
        #     self.dp[index][i] = result
        #     i += 1

        while i < len(string):
            sub_str = string[index:i+1]
            if self.search_trie(sub_str):
                result |= self.words(i+1, string)
            i += 1
        return result

    def search_trie(self, word):
        root = self.trie
        for letter in word:
            if letter in root:
                root = root[letter]
            else:
                return False
        else:
            if '_end_' in root:
                return True
            else:
                return False

    @staticmethod
    def get_trie(words):
        root = {}
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})

            current_dict['_end_'] = '_end_'
        return root


s = 'myinterviewtrainer'
dict = ["trainer", "my", "interview"]

# s = 'baaaaabbabaaababaabbbba'
# dict = [ "aaa", "abbabbbabb", "bbaaababa", "aba", "bab", "bba", "baa", "aa", "baabaaaaa", "ababbaaaa", "aaaaaa", "b", "aaabb", "aaaaba", "babbbaaba", "b", "babbb", "bbaaaaa", "bbaaa", "baaaaaa", "aa", "aaabba", "baaabaa", "bbabbab", "abbb", "bbabbb", "aaabaaa", "a", "aaabbabbaa", "baaaaab", "baabbbab", "ba", "baab" ]
#
# s = "aaaabbbbababbaababbbabbabaaabbaaaabbababbaabababaabbbababaaababbbbbaaababababbbbbaaaabbabbabaabbababbaaaaabbaababababbbaaaabaaabaabaababbabaaabaaababababbaabbbbbaabbabbaaaaabbabbbabbbbaaaaabababbaababbabbbabbbababaabaababbbaaaaababababbaabaabaabbbbaaabbbbbbababbabbabaabbaababbbbbbabaababbbbababbabbbbbbabbbbbbaabbbbbbabaabbabaabbbaaaababaababbbabaabbbbabbbbbbbababbaabbbaaabaabaabaabbbab"
# dict = [ "bbabaaaaba", "abbaa", "bbabbaaba", "bbaabbab", "ab", "b", "abaaaababa", "aa", "babaa", "aaa", "baa", "ab", "baaabbbba", "aaaba", "a", "bbaababaab", "baaaaaaa", "aaab", "bbabbbbaaa", "ab", "aaa", "bbb", "a", "bab", "aaaaaa", "aa", "b", "ababaabbb", "bbb", "babbbbba", "bbabb", "ab", "a", "baabaabbb", "aaabab", "aba", "a", "babba", "aaaababbbb", "b", "baab", "baabbbb", "babbb", "ababaa", "babbaa", "abaaa", "babababab", "bab", "aa", "abbaa", "abb", "bbbaaaaba", "bbbabababb", "aaaa", "ba", "bbaabbbaab", "bababb", "bbbb", "baaabbaab", "bababbbaaa", "bbaab", "ab", "bbbaaa", "aaaa", "aab", "baabaabaa", "bb", "ba", "bbbb", "abbaababab", "baaaaaa", "baaabbbb", "baab" ]


# s = "babbbbaabbaabaabaabaaabaababaaaabbbbbabbaabbabbbbababaabbabbbabbbaaabaababaaaababbbbabbbbbbaaaabaaabaabbbaaaabaaabbbaabababbbaaaabbabbbabaaabbbabaaabbbaaaaaabaabbabbaabbbbbaababbbbabbabbaabbbabaababaaaabbaabbbaabaabbbbbbaabbbaaaabbaaaaaabaabbaababbbabbbbbbaabbaabbbabbbaabbbaaaabbbaaaabbbabbaababaaabbababbaabbabbabaabbbbaaaabbaababababbbbbabbbbabbaaabbaabaaaaabbaaaaaaaaaaababaaabbbaababbbbbbbabbababbaabbaaaababbbabbaaabbbbbabbbaabbaaaaabbbbbbabbbbbabbabbbabbabbababbabaabaabbabababbababaababbaababbabaabbaaaabbbaa"
# dict = [ "bbba", "aaaa", "abaa", "aba", "aabaaa", "baabbaab", "bbbabbbaaa", "abaabbbbba", "abaa", "aba", "bbabbbbabb", "aab", "baaabbbaaa", "b", "baba", "aaba", "baaba", "abb", "aaaa", "baaabbbaa", "ab" ]



s = "aababaaabaaababbbabbbaabababaaabbaabaabbabbaabbbbbbbabbbbabaaabaabaabbaaaaabbabaababbbabbbbbbaaaabbbaaaaaabaaaaaabbbbbbbabbbbbbbbaaabaaababbbaaaabaaaabaaaabbabbbabaabbabbabaaaabbabaaabbabbabbbabbabbaabbbabaabaabbbbbbbaabababbbbbbababbbaabaabbbabababbbbbaaaababbbabaaabaabbaababbbabbbbbaabbaaaaabbbbbaaaaaaaaaaaabbabbbabbaaabaaaaaabaabababaabaaaabaaabbbbbaaabbaabbababbabbbbaabaabaabaaaabbbaababbaabbbbbabaaababbabbbabbbbbabaababbbbbaabbbbabaabbabbababaaaabbbbabbbaaaabaabbbbaaaaababaaabaabbabaababbabbbababaaababbaabbbaaabaabbbaabbbbbbaaabaabbbbbabaaababaaabbbbbbaaaabababaaabbbbbbaabbaaabbbabaabbabababbabaabbaaabbaaabbaabbbbbababbaabbabbb"
dict = [ "baaaaaabba", "babbaababb", "abb", "bababaabab", "baaa", "ab", "ab", "bb", "abbaaaa", "bbababa", "bbbbbbab", "abbaaabba", "aaaabbab", "abaaab", "babab", "aabaaab", "aabaabbabb", "aa", "bb", "ab", "a", "a", "bbaaab", "aba", "ba", "bbabbaabab", "aaabbbbbb", "abbaaaabbb", "aabaabbaa", "bbba", "abbabbba", "abbbbabb", "bbaaba", "abbbbaab", "bba", "bbbbaabba", "ababbabaab", "baabba", "ababbaabb", "bbaab", "a", "bbba", "aaaa", "aaabbbabba", "bab", "baaaabaa", "ab", "aaabbaab", "bab", "aa", "ababababab", "aabbaaaba", "abbaaba", "bbaabaa" ]

print Solution().wordBreak(s, dict)