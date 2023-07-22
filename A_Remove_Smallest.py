t = int(input())
for _ in range(t):
    def removeSmallest():
        n = int(input())
        nums = list(map(int, input().split()))

        i = 1
        nums.sort()
        while i < n:
            if nums[i] == nums[i-1] or nums[i] == nums[i-1] + 1:
                i += 1
            else:
                return "NO"
        return "YES"
    print(removeSmallest())
    
            

       