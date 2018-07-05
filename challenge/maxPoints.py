#Given number of matches, number of Goals scored
# 	number of Goals scored against
#Calculate max points possible for the team

#Greedy approach
def maxPoints(matches, goalsFor, goalsAgainst):
    m = 0
    while matches > 1:
        if goalsFor > 0:
            goalsFor-=1
            m+=3
        else:
            m+=1
        matches-=1
    if goalsFor>goalsAgainst:
        m+=3
    if goalsFor==goalsAgainst:
        m+=1
    return m
