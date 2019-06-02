# -*- coding: utf-8 -*-
'''
Module for text decoding.
'''
import random
import copy
import textstatistics


def encode_text(text, code):
    '''
Encodes the text with a substitution cipher defined with the code.
Argument "code" is a dictionary with characters as keys
and corresponding coding characters as values.
For example: 
code = {'a': 'z', 'b': 'y' , 'c': 'x'}
'''
    result = []
    for char in text:
        encoded_char = code.get(char, char)
        result.append(encoded_char)
    return u''.join(result)


def evalutate_decoding(text, language):
    '''
    Evaluates how the decoded text corresponds to the language.
    Returns estimated fitness as a float value from the range [0; 1], where
    0 means doesn't correspond at all,
    1 means all words are correct.
    '''
    fitness_sum = 0.0
    words = textstatistics.split_to_words(text)
    for word in words:
        fitness_sum += language.word_fitness(word)
    return fitness_sum / len(words)
 
def decode_text(text, language, treasure=0.99):
    '''
   Decodes the text encoded with a substitution cipher
   '''
    alphabet = language.get_alphabet()
    gener_key_alph = [x for x in alphabet.keys() if x != ' ' and x != ',' and x != '.']
    mix_alph = list(gener_key_alph)
    random.seed()
    random.shuffle(mix_alph)
    key = dict(zip(gener_key_alph, mix_alph))
    decoded_text = encode_text(text, key)
    rate = evalutate_decoding(decoded_text, language)
    while rate < treasure:
        new_key = copy.copy(key)
        random.seed()
        first_value = random.choice(list(new_key.keys())) #Get new key
        second_value = random.choice(list(new_key.keys()))
        buf = new_key[first_value]
        new_key[first_value] = new_key[second_value]
        new_key[second_value] = buf
        decoded_text = encode_text(text, new_key)
        new_rate = evalutate_decoding(decoded_text, language)
        if new_rate > rate: # check rating 
            rate = new_rate
            key = new_key
    decoded_text = encode_text(text, key)
    return decoded_text