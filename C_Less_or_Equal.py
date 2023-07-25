n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
for i in range(len(nums)):
    while i < k:
        if