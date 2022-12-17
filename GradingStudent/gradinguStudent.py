def gradingStudents(grades):
    # Write your code here
    arr = []
    for i in range(len(grades)):

        if grades[i] < 38:
            arr.append(grades[i])
        else:
            val = grades[i] % 5
            if (5 - val) < 3:
                grades[i] += 5-val
                arr.append(grades[i])
            else:
                arr.append(grades[i])
    return arr
