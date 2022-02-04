from itertools import count
from typing import List

# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
# You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        common_letters = []
        word_dict = self.get_word_dict(words)
        print(word_dict)
        unique_letters = self.get_unique_letters(words)
        for letter in unique_letters:
            for i in range(self.letter_count_in_words(letter, word_dict)):
                common_letters.append(letter)
        return common_letters

    def letter_count_in_words(self, letter, word_dict):
        occurrences = []
        for word in word_dict:
            if letter in word:
                occurrences.append(word_dict[word][letter])
        if len(occurrences) == len(word_dict):
            return min(occurrences)
        return 0

    def get_word_dict(self, words):
        word_dict = {}
        for word in words:
            word_dict[word] = {}
            for character in word:
                if character in word_dict[word]:
                    word_dict[word][character] += 1
                else:
                    word_dict[word][character] = 1
        return word_dict

    def get_unique_letters(self, words):
        unique_letters = []
        for word in words:
            for letter in word:
                if letter not in unique_letters:
                    unique_letters.append(letter)
        return unique_letters

sol = Solution()
common_letters = sol.commonChars(["bella","label","roller"])
print(common_letters)
