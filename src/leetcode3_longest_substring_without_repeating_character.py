def length_of_longest_substring(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        # If char is seen and within current window, jump 'start'
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1

        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
        print(char_map)
    return max_length
    # solution 2: sliding window 
    # left = 0 
    # max_length = 0
    # # record repeated char
    # char_set = set()
    # for right in range(len(s)): 
    #     # remove duplicate characters
    #     while s[right] in char_set: 
    #         char_set.remove(s[left])
    #         left += 1
    #     # add the character to track repeated char
    #     char_set.add(s[right])
    #     max_length = max(max_length, (right - left + 1))
    # return max_length
length_of_longest_substring("abcabcbb")
