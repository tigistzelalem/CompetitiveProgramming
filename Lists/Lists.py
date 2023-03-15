if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        l = input().split()

        if l[0] == 'insert':
            arr.insert(int(l[1]), int(l[2]))
        if l[0] == 'print':
            print(arr)
        if l[0] == 'remove':
            arr.remove(int(l[1]))
        if l[0] == 'append':
            arr.append(int(l[1]))
        if l[0] == 'sort':
            arr.sort()
        if l[0] == 'reverse':
            arr.reverse()
        if l[0] == 'pop':
            arr.pop()
