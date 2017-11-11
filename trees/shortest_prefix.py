class Solution:
    # @param A : list of strings
    # @return a list of strings

    @staticmethod
    def get_prefix(trie, words):

        def singular(current_dict, rem):
            for letter in rem:
                current_dict = current_dict[letter]
                if len(current_dict) > 1:
                    return False
            return True


        final = []

        for word in words:
            prefix = ''
            current = trie
            for i, letter in enumerate(word):
                prefix += letter
                current = current[letter]
                if len(current) == 1 and singular(current, word[i+1:]):
                    final.append(prefix)
                    break

        return final

    @staticmethod
    def make_trie(words):
        root = {}
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict['_end_'] = '_end_'

        return root

    def prefix(self, A):

        trie = self.make_trie(A)

        # print trie

        final = self.get_prefix(trie, A)

        return final


A = [ "zebra", "dog", "duck", "dot" ]
A = [ "bearcat", "bert" ]

print Solution().prefix(A)