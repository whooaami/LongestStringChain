import unittest

from wchain import read_data
from wchain import longest_string_chain


class LongestStringChainTest(unittest.TestCase):

    def test_positive_wchain(self):
        data = read_data('wchain_1.in')
        expected = 6

        self.assertEqual(longest_string_chain(data), expected)

    def test_positive_wchain_2(self):
        data_2 = read_data('wchain_2.in')
        expected = 4

        self.assertEqual(longest_string_chain(data_2), expected)

    def test_positive_wchain_3(self):
        data_3 = read_data('wchain_3.in')
        expected = 1

        self.assertEqual(longest_string_chain(data_3), expected)

    def test_wrong_wchain(self):
        data = read_data('wchain_1.in')
        expected = 3

        self.assertNotEqual(longest_string_chain(data), expected)


if __name__ == '__main__':
    unittest.main()