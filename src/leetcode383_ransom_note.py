class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # can ransomNote construct from the letter from magazine? 
        # record the appearance for each of the character in magazine
        characters = {}
        for char in magazine: 
            characters[char] = characters.get(char, 0) + 1
        # for every character in ransom note, if the character is in the characters array, minus the appearance by 
        for character in ransomNote: 
            if character in characters.keys():
                if characters[character] > 0: 
                    characters[character] -= 1
                else: 
                    return False
        # if the appearance is 0, or the characters not found, return false, or vice versa. 
            else: 
                return False 
        return True


if __name__ == "__main__": 
    solution = Solution()
    ransomNote = 'haha'
    magazine = 'aah'
    print(solution.canConstruct(ransomNote=ransomNote, magazine=magazine))
