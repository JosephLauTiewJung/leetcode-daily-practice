import unittest
from leetcode5_longest_palindrome_substring import Solution
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_longest_palindrome(self):
        solution = Solution()
        result: str = solution.longestPalindrome("babad")
        print(result)
        self.assertEqual("bab", result)
if __name__ == '__main__':
    unittest.main()
