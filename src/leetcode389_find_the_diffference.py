class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # xor approach 
        # x ^= x = 0
        # x ^= 1 = x
        # constraint: only one letter differene and the letter is always in the end of the sentence
        result = 0
        for char in s: 
            result ^= ord(char)
            print(f'result: {result}, char: {char}')
        for  char in t: 
            result ^= ord(char)
            print(f'result: {result}, char: {char}')
        return chr(result)

if __name__ == '__main__': 
    solution = Solution()
    print(solution.findTheDifference("abc", "abcd"))