import collections
import sys
import re
import difflib

def get_item_frequencies(sequence):
    result = collections.defaultdict(int)
    for item in sequence:
        result[item] += 1
    return result

def get_char_frequencies(text):
    return get_item_frequencies(text)

def split_to_words(text):
    raw_word_list = re.split(r"\W", text, flags=re.UNICODE)
    result = [word for word in raw_word_list if word] # Get rid of empty items
    return result

def get_word_frequencies(text):
    return get_item_frequencies(split_to_words(text))

class Languauge:
    '''
    Class representing particular language with alphabet and dictionary
    '''

    def __init__(self, alphabet, dictionary):
        self.__alphabet = alphabet
        self.__dictionary = dictionary

    def get_alphabet(self):
        return self.__alphabet

    def compare(self, word1, word2):
        return difflib.SequenceMatcher(None, word1, word2).ratio()

    def word_fitness(self, word):
        return max([self.compare(word, dict_word)
                    for dict_word in self.__dictionary])


def main():
    print(get_char_frequencies(u"а-с"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
