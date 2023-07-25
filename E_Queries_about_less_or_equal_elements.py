n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(len(a)-1):
    count = 0
    for j in range(len(b)-1):
        if b[i] > a[j]:
            count += 1
print(count)
        
