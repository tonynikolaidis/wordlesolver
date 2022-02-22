"""
Load words into Python

Code taken from https://github.com/dwyl/english-words/blob/master/read_english_dictionary.py
"""

import json


def load_words():
    with open("dictionary.txt") as word_file:
        # valid_words = set(word_file.read().split())
        valid_words = json.load(word_file)

    return valid_words
