class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        # O(1)
        if len(t) != len(s):
            return False

        # O(n)
        for i in range(len(s)):
            if s[i] in characters:
                characters[s[i]] += 1
            else:
                characters[s[i]] = 1

        # O(n)
        for i in range(len(t)):
            if t[i] in characters and characters[t[i]] > 0:
                characters[t[i]] -= 1
            else:
                return False
        return True

    ## T(n) = 2n