#  if it works, it works.
#  Copyright Nathan Duranel, 2021
#  Distributed under the terms of the license GNU GPLv3, detailled in LICENSE

__version__ = "0.1"
__author__ = "The_ZmaZe - github.com/The-ZmaZe/"


import string
import random
from typing import Iterable, NoReturn


ALPHABET = tuple(string.ascii_lowercase)
VOWELS = ("a", "e", "i", "o", "u", "y")
CONSONANTS = tuple(letter for letter in ALPHABET if not(letter in VOWELS))


class CulturalGroup():
    """Encapsulate a cultural group of languages
    """
    def __init__(self, syllables_dict, words_length):
        self.syllables_dict = syllables_dict
        self.words_length = words_length

    def generator(self, n) -> tuple:
        """Generate n words according to current CulturalGroup's args
        """
        words = list()

        for i in range(n):
            word = ""
            current_syllables = self.syllables_dict
            word_length = random.choices(tuple(self.words_length.keys()),
                                         weights=self.words_length.values(),
                                         k=1)
            for i in range(word_length[0]):
                syllable = random.choices(tuple(current_syllables.keys()),
                                          weights=current_syllables.values(),
                                          k=1)[0]
                word += syllable
                current_syllables[syllable] -= 1

                if syllable[2] in VOWELS:
                    for element in tuple(current_syllables.keys()):
                        if element[0] in CONSONANTS:
                            current_syllables[element] += 1

                if syllable[2] in CONSONANTS:
                    for element in tuple(current_syllables.keys()):
                        if element[0] in CONSONANTS:
                            current_syllables[element] -= 0.5
                        if element[0] in VOWELS:
                            current_syllables[element] += 1

                for element in tuple(current_syllables.keys()):
                    if element[0] == syllable[2]:
                        current_syllables[element] -= 1

                #print(current_syllables)


            words.append(word)
        return tuple(words)


def syllables_lister() -> tuple:
    return tuple(elem.rstrip().lower()
        for elem in open("3letterwords", "r").readlines())

def structure_generator(syllables_list: Iterable[str]=syllables_lister(),
                        vowels_weight: int=5,
                        consonants_weight: int=3,
                        **weight) -> tuple[dict]:
    """Generate randomly and return a tuple containing:
        0: syllables_dict
        1: words_length

        Parameters:
            syllables_list - Iterable[str] - syllables
            vowels_weight - int - base weight of vowels
            consonants_weight - int - base weight of consonants
            weight - specific weight of a letter, example: a=2
    """
    weights_list = list()
    for letter in ALPHABET:
        if letter in VOWELS:
            if letter in tuple(weight.keys()):
                weights_list.append(vowels_weight + int(weight[letter]))
            else:
                weights_list.append(int(vowels_weight))
        else:
            if letter in tuple(weight.keys()):
                weights_list.append(consonants_weight + int(weight[letter]))
            else:
                weights_list.append(int(consonants_weight))
    weights = dict(zip(ALPHABET, weights_list))

    syllables_dict = dict(zip(syllables_list,
        (random.randint(1,5) for i in range(len(syllables_list)))))
    # print(syllables)
    # print(syllables_dict)
    weights_list = ((1, 3, 2, 2),
                    (1, 2, 3, 1),
                    (1, 3, 2, 1),
                    (2, 3, 2, 1),
                    (2, 3, 2, 1),
                    (3, 3, 2, 1),
                    (3, 3, 1, 1),
                    (4, 3, 1, 0))

    words_length = {i+1: random.choices((1, 2, 3, 4), weights=elem, k=1)[0]
            for i, elem in enumerate(weights_list)}

    return syllables_dict, words_length


# bad results (for now)
def syllable_gen(weights: dict) -> str:
    """Return 3 letter syllable
        Parameter:
            weights - dict - contain all letters as keys and weight as value
    """
    syllable = str()
    curr_weights = weights
    for i in range(3):
        letter = random.choices(tuple(weights.keys()),
                                tuple(curr_weights.values()))[0]
        syllable += letter

        curr_weights = weights
        if letter in VOWELS:
            for element in tuple(weights.keys()):
                if element in CONSONANTS:
                    curr_weights[element] += 2
                else:
                    curr_weights[element] -= 1
        else:
            for element in tuple(weights.keys()):
                if element in CONSONANTS:
                    curr_weights[element] -= 1
                else:
                    curr_weights[element] += 1
    return syllable



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

    group_a = CulturalGroup(syllables, words_length)
    print(group_a.generator(10))

    a, b = structure_generator()
    group_b = CulturalGroup(a, b)
    print(group_b.generator(10))