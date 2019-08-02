from collections import Counter, defaultdict


class Solution:
    def __init__(self):
        self.ana_letters = {}
        self.ana_groups = defaultdict(list)

    def get_letters(self, word):
        my_letters = Counter()
        for letter in word:
            my_letters[letter] += 1
        self.ana_letters[word] = my_letters

    def solver(self, list_of_words):
        for word in list_of_words:
            self.get_letters(word)
            found = False
            for group in self.ana_groups:
                if self.ana_letters[group] == self.ana_letters[word]:
                    self.ana_groups[group].append(word)
                    found = True
            if not found:
                self.ana_groups[word].append(word)

        result = []
        for key in self.ana_groups:
            result.extend(self.ana_groups[key])

        return result



list_of_words = [
    "abc", "cba", "aab", "aba", "fgh"
]

s = Solution()
l = s.solver(list_of_words)
print(l)
