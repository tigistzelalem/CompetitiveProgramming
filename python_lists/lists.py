if __name__ == '__main__':
    N = int(input())
    res = []
    for val in range(N):
        val = input().split()

        if val[0] == "insert":
            res.insert(int(val[1]), int(val[2]))
        elif val[0] == "remove":
            res.remove(int(val[1]))
        elif val[0] == "append":
            res.append(int(val[1]))
        elif val[0] == "pop":
            res.pop()
        elif val[0] == "sort":
            res.sort()
        elif val[0] == "reverse":
            res.reverse()
        elif val[0] == "print":
            print(res)
