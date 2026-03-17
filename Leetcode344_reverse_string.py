from typing import List
import time
def main():
    start_time = time.time()
    s: List[str] = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)
    end_time = time.time()
    print(f'total time: {(end_time - start_time) * 1000}s')

def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    temp_value = ''
    l = 0
    r = len(s) - 1
    while l < r:
        temp_value = s[l]
        s[l] = s[r]
        s[r] = temp_value
        l += 1
        r -= 1
if __name__ == "__main__":
    main()