def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleys = 0
    in_vallet = False
    for i in range(steps):
        if path[i] == 'U':
            altitude += 1
        else:
            altitude -= 1
        if altitude < 0:
            in_vallet = True
        if altitude == 0 and in_vallet:
            valleys += 1
            in_vallet = False
    return valleys
