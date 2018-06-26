# given an array of time estimated for each presentation/student
# and a group size (or parallel presentations)
# calculate the minimum time required to get all presentation done

def assignGroups(timeEstimates,groupSize):
    if not timeEstimates:
        return 0
    minEst = 0
    timeEstimates.sort(reverse=True)
    for i in range(0,len(timeEstimates),groupSize):
        minEst+=timeEstimates[i]

    return minEst