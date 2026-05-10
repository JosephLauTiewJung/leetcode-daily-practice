class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for size in range(1, len(s) // 2 + 1):
            # try possible length of substring that could be repeated to make the full string 
            if len(s) % size == 0:
                substring = s[:size]
                # append the substring until it matches the size of the word, then compare it with the word 
                if substring * (len(s) // size) == s:
                    return True
        return False
if __name__ == '__main__': 
    solution = Solution()
    # # test case 1: "abab" -> true
    # print(solution.repeatedSubstringPattern("abab")) 
    # # test case 2: "aba"  -> false 
    # print(solution.repeatedSubstringPattern("aba")) 
    # test case 3: "abcabcabcabc" -> true
    print(solution.repeatedSubstringPattern("abcabcabcabc")) 
