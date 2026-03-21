class Solution:
    def longestPalindrome(self, s: str) -> str:
        start: int = 0
        end: int = 0
        # exception case
        if not s:
            return ""
        for i in range(len(s)):
            # Check for odd-length palindromes (e.g., "aba")
            len1 = self.expandAroundCenter(s, i, i)
            # Check for even-length palindromes (e.g., "bb")
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1