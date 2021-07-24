#  if it works, it works.
#  Copyright Nathan Duranel, 2021
#  Distributed under the terms of the license GNU GPLv2, detailled in LICENSE

__version__ = "0.1"
__author__ = "The_ZmaZe - github.com/The-ZmaZe/"


import string
import random
from typing import NoReturn


ALPHABET = tuple(string.ascii_lowercase)
VOWELS = ("a", "e", "i", "o", "u", "y")
CONSONANTS = tuple(letter for letter in ALPHABET if not(letter in VOWELS))


class CulturalGroup():
    """Encapsulate a cultural group of languages
    """
    def __init__(self, syllable_dict, words_length):
        self.syllable_dict = syllable_dict
        self.words_length = words_length

    def generator(self, n) -> tuple:
        """Generate nb words according to current CulturalGroup's args
        """
        words = list()

        for i in range(n):
            word = ""
            current_syllables = self.syllable_dict
            word_length = random.choices(list(self.words_length.keys()),
                                         weights=self.words_length.values(),
                                         k=1)
            for i in range(word_length[0]):
                syllable = random.choices(list(current_syllables.keys()),
                                          weights=current_syllables.values(),
                                          k=1)[0]
                word += syllable
                current_syllables[syllable] -= 1

                if syllable[2] in VOWELS:
                    for element in list(current_syllables.keys()):
                        if element[0] in CONSONANTS:
                            current_syllables[element] += 1

                for element in list(current_syllables.keys()):
                    if element[0] == syllable[2]:
                        current_syllables[element] -= 1

            words.append(word)
        return tuple(words)


if __name__=="__main__":
    syllables = {
        "arc": 3,
        "erk": 1,
        "roc": 2,
        "rea": 2,
        "rou": 4,
        "cro": 3,
        "lou": 4,
        "lau": 4,
        "dro": 3,
        "zor": 2,
        "tro": 2,
        "mau": 3,
        "sau": 3,
        "ope": 3,
        "shi": 3,
        "uni": 4,
        "pol": 3,
        "sor": 3,
        "zer": 2,
        "for": 2,
        "per": 3,
        "zou": 2,
        "ric": 2,
        "bio": 2,
        "lay": 2

    }

    words_length = {
        1: 3,
        2: 4,
        3: 3,
        4: 4,
        5: 2,
        6: 2,
        7: 1,
        8: 1
    }

    group = CulturalGroup(syllables, words_length)
    print(group.generator(10))