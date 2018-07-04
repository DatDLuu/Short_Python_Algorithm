# draws and wins challenge
# or combinations of 1 and 3 such that their sum = points
# and their count less than teams
def drawsAndWins(teams, points):
    result = []
    for i in range(points+1):
        if (points-i)%3==0 and (i+(points-i)/3<=teams-1):
            result.append([i,(points-i)/3])
    return result


    '''
    # Out of mem recursion with max val input
    # 
    result = set()
    seen = set()
    def recurP(m,p,d,w,pp):
        if m < 0:
            return
        else:
            if p < pp:
                if (d,w) not in seen:
                    seen.add((d,w))
                    recurP(m-1,p+1,d+1,w,pp)
                    recurP(m-1,p+3,d,w+1,pp)
                return
            elif (d+3*w == points):
                result.add((d,w))
                return
            else:
                return
            
    recurP(teams-1,0,0,0,points)
    
    return sorted([[x,y] for x,y in result])
    '''
