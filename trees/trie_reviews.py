class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_words = A.split('_')

        good_trie = self.make_trie(good_words)

        res = dict()

        for i, review in enumerate(B):
            count = 0
            r = review.split('_')
            for word in r:
                if self.search_word(good_trie, word):
                    count += 1

            if res.has_key(count):
                res[count].append(i)
            else:
                res[count] = [i]

        final = list()
        for x in sorted(res.keys(), reverse=True):
            final += res[x]

        return final

    @staticmethod
    def make_trie(words):
        root = {}

        for word in words:
            current = root
            for letter in word:
                current = current.setdefault(letter, {})
            current['_end_'] = '_end_'

        return root

    @staticmethod
    def search_word(trie, word):
        current = trie
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                return False
        else:
            if '_end_' in current:
                return True
            else:
                return False

A = "cool_ice_wifi"
B = [ "water_is_cool", "cold_ice_drink", "cool_wifi_speed" ]

print Solution().solve(A, B)
