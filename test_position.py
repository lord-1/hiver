import unittest
from nose_parameterized import parameterized
from rover import Position


class TestPosition(unittest.TestCase):

    def setUp(self):
        self.pos = Position()

    def tearDown(self):
        del self.pos

    def test_1(self):
        self.assertEqual(Position().get(), (0, 0, 'North'))

    @parameterized.expand([
        [True, None, (0, 1, 'North')],
        [False, "L", (0, 0, 'West')],
        [False, "R", (0, 0, "East")],
        [True, "L", (0, 1, "North")]
    ])
    def test_2(self, movement, face, output):
        self.pos.set(face, movement)
        self.assertEqual(output, self.pos.get())
