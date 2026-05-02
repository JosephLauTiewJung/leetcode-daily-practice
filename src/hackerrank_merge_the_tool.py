def merge_the_tools(string, k):
    # your code goes here
    # split the into substring with k letters, and return the unique letter 
    # we can use sliding windows
    substrings = []
    p1 = 0
    p2 = p1 + k 
    while p2 < len(string) + 1: 
        substring = ''
        appeared_char = ''
        for i in range(p1, p2): 
            if string[i] not in appeared_char: 
                appeared_char += string[i]
                substring += string[i]
        print(substring)
        p1 += k 
        p2 += k 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)