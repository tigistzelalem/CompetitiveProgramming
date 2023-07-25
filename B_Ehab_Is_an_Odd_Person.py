
n = int(input())
arr = list(map(int, input().split()))

odd = sum(1 for x in arr if x % 2 == 1)

if odd > 0 and odd < n:
    arr.sort()
print(*arr)
