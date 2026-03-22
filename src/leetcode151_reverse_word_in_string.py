class Solution:
    def reverseWords(self, s: str) -> str:
        # Solution 1: allow using built-in function
        # split into list 
        # str_list = s.split()
        # # reverse each word
        # str_list.reverse()
        # print(str_list)
        # # join back to string
        # return " ".join(str_list)
        # Solution 2: double pointer
        str_list = list(s)
        # clean the leading and trailing space 
        trimmed = []
        left = 0
        right = len(str_list) - 1
        while left <= right and str_list[left] == ' ':
            left += 1
        while left <= right and str_list[right] == ' ': 
            right -= 1 
        # clean extra internal spaces
        while left <= right: 
            if str_list[left] != ' ': 
                trimmed.append(str_list[left])
            elif str_list[left] == ' ' and trimmed[-1] != ' ': 
                trimmed.append(str_list[left])
            left += 1
        # reverse the string 
        def reverse_range(arr, left, right): 
            while left < right: 
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        reverse_range(trimmed, 0, len(trimmed) - 1)
        # reverse the individual word 
        start = 0
        for end in range(len(trimmed) + 1): 
            if end == len(trimmed) or trimmed[end] == " ": 
                reverse_range(trimmed, start, end - 1)
                start = end + 1

        # join 
        return "".join(trimmed)
