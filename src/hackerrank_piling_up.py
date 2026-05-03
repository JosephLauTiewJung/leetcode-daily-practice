# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    top = float("inf")
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            pick = blocks[left]
            left += 1
        else:
            pick = blocks[right]
            right -= 1

        if pick > top:
            possible = False
            break

        top = pick

    print("Yes" if possible else "No")
