
import unittest
from src.main import find_longest_sequence


class TestFindLongestSequences(unittest.TestCase):
    def test_with_no_match(self):
        my_list = ["word", "anotherword", "yetanotherword"]
        result = find_longest_sequence(my_list)
        self.assertEqual(result, 1)

    def test_with_first_shortest_first_letter(self):
        my_list = ["b", "bcad", "bca", "bad", "bd"]
        result = find_longest_sequence(my_list)
        self.assertEqual(result, 4)

    def test_with_first_longest_letter(self):
        my_list = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        result = find_longest_sequence(my_list)
        self.assertEqual(result, 6)
