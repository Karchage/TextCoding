# -*- coding: utf-8 -*-
'''
Tests for textstatistics module
'''

import unittest
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(root_path)

import textstatistics

QUOTE_FROM_TOLSTOY = \
        u'Не слушайте тех, кто говорит дурно о других и хорошо о вас.'
QUOTE_FROM_SHAKESPEARE= "To be, or not to be?"

class TestGetCharFrequencies(unittest.TestCase):
    def test_get_char_frequencies_empty(self):
        text = u''
        result = textstatistics.get_char_frequencies(text)
        expected = {}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_uniform(self):
        text = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
        result = textstatistics.get_char_frequencies(text)
        expected = {char: 1 for char in text}
        self.assertDictEqual(result, expected)

    def test_get_char_frequencies_simple_text(self):
        text = QUOTE_FROM_TOLSTOY
        result = textstatistics.get_char_frequencies(text)
        expected = {
                    u'Н': 1,
                    u'е': 3,
                    u' ': 11,
                    u'с': 2,
                    u'л': 1,
                    u'у': 3,
                    u'ш': 2,
                    u'а': 2,
                    u'й': 1,
                    u'т': 4,
                    u'х': 3,
                    u',': 1,
                    u'к': 1,
                    u'о': 9,
                    u'г': 2,
                    u'в': 2,
                    u'р': 4,
                    u'и': 3,
                    u'д': 2,
                    u'н': 1,
                    u'.': 1,
                    }
        self.assertDictEqual(result, expected)


class TestWordFunctions(unittest.TestCase):
    def test_split_to_words_english(self):
        text = QUOTE_FROM_SHAKESPEARE
        expected = ['To', 'be', 'or', 'not', 'to', 'be']
        result = textstatistics.split_to_words(text)
        self.assertEqual(result, expected)

    def test_split_to_words_russian(self):
        text = QUOTE_FROM_TOLSTOY
        expected = [
                    u'Не',
                    u'слушайте',
                    u'тех',
                    u'кто',
                    u'говорит',
                    u'дурно',
                    u'о',
                    u'других',
                    u'и',
                    u'хорошо',
                    u'о',
                    u'вас'
                    ]
        result = textstatistics.split_to_words(text)
        self.assertEqual(result, expected)

    def test_get_word_frequencies_empty(self):
        text = ''
        expected = {}
        result = textstatistics.get_word_frequencies(text)
        self.assertEqual(result, expected)

    def test_get_word_frequencies_english(self):
        text = QUOTE_FROM_SHAKESPEARE
        expected = {'To': 1, 'be': 2, 'or': 1, 'not': 1, 'to': 1}
        result = textstatistics.get_word_frequencies(text)
        self.assertDictEqual(result, expected)

    def test_get_word_frequencies_russian(self):
        text = QUOTE_FROM_TOLSTOY
        expected = {
                    u'Не': 1,
                    u'слушайте': 1,
                    u'тех': 1,
                    u'кто': 1,
                    u'говорит': 1,
                    u'дурно': 1,
                    u'о': 2,
                    u'других': 1,
                    u'и': 1,
                    u'хорошо': 1,
                    u'вас': 1
                    }
        result = textstatistics.get_word_frequencies(text)
        self.assertDictEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
