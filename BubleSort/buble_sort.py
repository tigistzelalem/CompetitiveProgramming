def countSwaps(a):
    # Write your code here
    sortCount = 0
    for i in range(len(a)):
        for j in range(0, len(a) - 1):
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                sortCount += 1
    print("Array is sorted in", sortCount, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
