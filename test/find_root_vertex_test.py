
import unittest
from main import find_root_vertex


class TestFindPeakSequences(unittest.TestCase):
    def test_all_vertex_root(self):
        graph = {
            0: [4],
            1: [0],
            2: [1, 4],
            3: [2, 1],
            4: [3]
        }
        result = find_root_vertex(graph)
        self.assertEqual(result, 0)

    def test_no_root(self):
        graph = {
            0: [1, 2],
            1: [2],
            2: [],
            3: [4],
            4: []
        }
        result = find_root_vertex(graph)
        self.assertEqual(result, -1)

    def test_array_sorted_by_descending(self):
        graph = {
            0: [1],
            1: [2],
            2: [3],
            3: [0],
            4: [3, 5],
            5: [0]
        }
        result = find_root_vertex(graph)
        self.assertEqual(result, 4)
