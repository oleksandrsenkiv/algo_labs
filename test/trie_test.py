
import unittest
from src.main import create_trie, Trie


class TestTrie(unittest.TestCase):
    def test_create_trie(self):
        patterns = ["siren", "sky", "rock", "night"]
        trie = create_trie(patterns)
        self.assertIsInstance(trie, Trie)

    def test_find_word(self):
        patterns = ["siren", "sky", "rock", "night"]
        trie = create_trie(patterns)
        search_word1 = "sky"
        search_word2 = "tree"
        result1 = trie.find_word(search_word1)
        result2 = trie.find_word(search_word2)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    def test_find_prefix(self):
        patterns = ["siren", "sky", "rock", "night"]
        trie = create_trie(patterns)
        search_prefix1 = "sk"
        search_prefix2 = "tr"
        result1 = trie.find_prefix(search_prefix1)
        result2 = trie.find_prefix(search_prefix2)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
