'''
   RoboMaster is an international engineering / programming / eSports competition for university students. 
   The tournament is an annual event, with the finals taking place in Shenzhen, China.
   The rules are more complicated. This is just a simple simulation to calculate a winner based on
   a given list of shooting back and forth between two teams
'''

def roboMaster(shots):
    L = lambda x,y: 0 if x - y < 0 else x-y

    # define bots from red and blue team
    red = {"1" : 1000, "2" : 2000, "3" : 5000, "4" : 1000, "5" : 1000, "base" : 10000}
    blue = {"1" : 1000, "2" : 2000, "3" : 5000, "4" : 1000, "5" : 1000, "base" : 10000}

    # process damage calculation
    for i in shots:
        shot = i[0].split(" ")
        if (shot[0] == "red" and red[shot[1]]==0) or (shot[0]=="blue" and blue[shot[1]]==0):
            continue
        get_shot = i[1].split(" ")
        damg = 50 if i[2]=="17mm" else 500
        if get_shot[0] == "red":
            if get_shot[1]=="base" and not 0 in red.values():
                continue
            red[get_shot[1]]= L(red[get_shot[1]],damg)
            if red["base"]==0:
                return "blue"
            
        if get_shot[0] == "blue":
            if get_shot[1]=="base" and not 0 in blue.values():
                continue
            blue[get_shot[1]]=L(blue[get_shot[1]],damg)
            if blue["base"]==0:
                return "red"
            
    # determine winner based on team stat
    if red["base"]==blue["base"]:
        sum1 = sum2 = 0
        for i in ("1","2","3","4","5"):
            sum1+=red[i]
            sum2+=blue[i]
        if sum1 > sum2:
            return "red"
        elif sum2 > sum1:
            return "blue"
        else:
            return "draw"
    if red["base"]>blue["base"]:
        return "red"
    if blue["base"]>red["base"]:
        return "blue"
    return "f"
