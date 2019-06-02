# -*- coding: utf-8 -*-
'''
Tests for decode module
'''

import unittest
import os
import sys
import random


root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

import data
import decode
import textstatistics


class TestDecodeText(unittest.TestCase):
    def setUp(self):
        original_alphabet = list(u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

        self.original_text = data.QUOTE_FROM_ILF_AND_PETROV
        alphabet = textstatistics.get_char_frequencies(self.original_text)
        alphabet = {char: frequency for (char, frequency) in alphabet.items() if char in original_alphabet}
        dictionary = textstatistics.get_word_frequencies(self.original_text)
        self.language = textstatistics.Languauge(alphabet, dictionary)

        actual_original_alphabet = alphabet.keys()
        shuffled_alphabet = list(actual_original_alphabet)
        random.seed(1001)
        random.shuffle(shuffled_alphabet)
        self.code = dict(zip(actual_original_alphabet, shuffled_alphabet))

    def test_decode_text_same_rus(self):
        encoded_text = decode.encode_text(self.original_text, self.code)

        decoded_text = decode.decode_text(encoded_text, self.language)
        self.assertEqual(self.original_text, decoded_text)

    def test_decode_text_extract_rus(self):
        original_text_words = self.original_text.split()
        original_extract = ' '.join(
                    original_text_words[: len(original_text_words) // 2])
        encoded_extract = decode.encode_text(original_extract, self.code)

        decoded_extract = decode.decode_text(encoded_extract, self.language)
        self.assertEqual(original_extract, decoded_extract)


class TestEvalutateDecoding(unittest.TestCase):
    def test_evalutate_decoding_complete_eng(self):
        decoded_text = base_text = 'This is a sample text.'

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertEqual(result, 1.0)

    def test_evalutate_decoding_subset_eng(self):
        base_text = 'This is a sample text.'
        base_text_words = textstatistics.split_to_words(base_text)
        decoded_text = ' '.join(base_text_words[: len(base_text_words) // 2])

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertEqual(result, 1.0)

    def test_evalutate_decoding_almost_eng(self):
        base_text = 'This is a sample text.'
        decoded_text = 'Thas as i simple text.'

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertTrue(result < 1.0 and result > 0.5)


if __name__ == "__main__":
    unittest.main()
