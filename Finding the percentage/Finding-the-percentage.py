if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    arr = []
    for j in student_marks.values():
        avg = sum(j)/len(j)
    arr.append(avg)
    arr.sort(reverse=True)
    print("%.2f" % round(arr[len(arr)-1], 2))
