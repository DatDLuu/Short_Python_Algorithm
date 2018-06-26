# given a point on 2D plane find
# the point on its diagonal segment of given length
# function return the point from top right diag seg
import math
def diagSeg(xy,length):
    for x1 in range(xy[0]+1,xy[0]+length):
        dy = length**2-(x1-xy[0])**2
        if math.sqrt(dy)-int(math.sqrt(dy))==0:
            return [x1,int(math.sqrt(dy))+xy[1]]