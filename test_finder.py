import unittest
from nose_parameterized import parameterized
from word_finder import Finder


class TestCreateCharMap(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(
        [["sad", [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]],
         ["dasse", [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]],
         ["", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
    )
    def test_1(self, inp, output):
        self.assertEqual(output, Finder.create_char_map(inp))


class TestFinder(unittest.TestCase):

    @parameterized.expand([
        ["sad", ["das", "dasss", "wedsd"], ["das"]],
        ["w", ["a", "ww", "bfs"], []],
        ["helo", ["helodafdsfa", 'asdadrfdheloasd'], ["helodafdsfa", 'asdadrfdheloasd']]
    ])
    def test_1(self, inp, inp_set, output):
        self.assertEqual(output, Finder(inp_set).find(inp))

