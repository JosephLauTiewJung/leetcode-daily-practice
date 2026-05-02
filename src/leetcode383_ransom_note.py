class Solution:
    def buildCharacterMap(self, word): 
        characters = {}
        for char in word: 
            characters[char] = magazine.count(char)
        return characters
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # can ransomNote construct from the letter from magazine? 
        # record the appearance for each of the character in magazine
        magazine_char = self.buildCharacterMap(magazine)
        print(magazine_char)
        # if character number in ransomnote is not equal to the the character number in magazine
        # compare ransom unique character appearance in magazine_char 
        for character in set(ransomNote.split("")): 
            if ransomNote.count(character) > magazine_char[character]: 
                return false
            else: 
                return True

if __name__ == "__main__": 
    solution = Solution()
    ransomNote = 'haha'
    magazine = 'aahh'
    solution.canConstruct(ransomNote=ransomNote, magazine=magazine)
