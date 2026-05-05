class Solution:
    # time complexity: O(N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # build a new string with the sequence of word1[i] + word2[i]
        string_arr = []
        # determine the minimum word len 
        min_len = min(len(word1), len(word2))
        # if the words is shorter than longer word, to avoid the index out of word issue, we should use the index of the shorter word as pointer. 
        for i in range(0, min_len): 
            string_arr.append(word1[i])
            string_arr.append(word2[i])
        # concatenate the remainder character of the longer word to the new string
        string_arr.append(word1[min_len:])
        string_arr.append(word2[min_len:])
        return "".join(string_arr)
if __name__ == '__main__': 
    solution = Solution()
    print(solution.mergeAlternately("abc", "pqr"))
