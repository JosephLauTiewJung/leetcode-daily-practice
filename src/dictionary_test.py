import unittest


class MyTestCase(unittest.TestCase):
    def test_dictionary_behavior(self):
        sample_dict = {'a': 1, 'b': 2}
        sample_dict['c'] = sample_dict.get('c', 0) + 1
        self.assertEqual(sample_dict, {'a': 1, 'b': 2, 'c': 1})


if __name__ == '__main__':
    unittest.main()
