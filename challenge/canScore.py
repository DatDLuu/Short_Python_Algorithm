# given list of atk players and def players
# check if it's possible to pass the ball 
# 	from first atk player to last atk player
# without being intercepted by any def players

def canScore(atk_ps, def_ps, d):

    # check if line segment (p1 pos to p2 pos) 
    #       intersect with circle (def player pos as center and d as radius)
    # or player[i] can pass to player[j] without being intercept by given def_player
    # based on http://mathworld.wolfram.com/Circle-LineIntersection.html
    def can_pass(x1,y1,x2,y2,x3,y3,radius):
        px = x2 - x1
        py = y2 - y1
        u =  ((x3 - x1) * px + (y3 - y1) * py) / float(px*px + py*py)
        
        if u > 1:
            u = 1
        if u < 0:
            u = 0
            
        x = x1 + u * px
        y = y1 + u * py
        
        dx = x - x3
        dy = y - y3
    
        if math.sqrt(dx*dx+dy*dy) < radius:
	        return False
        return True
    
    # BFS to find possible pass from first to last atk_ps
    def can_score(g,s,e,path=[]):
        path = path + [s]
        
        if s == e:
            return path
        if not s in g:
            return None
        for i in g[s]:
            if i not in path:
                new_path = can_score(g,i,e,path)
                if new_path: return new_path
        return None
                    
    l = len(atk_ps) 
    graph = {k:[] for k in range(l)}

    # build indirected graph of pass
    # nested for loop is really sloppy
    for i,p1 in enumerate(atk_ps):
        for p2 in (atk_ps[:i]+atk_ps[i+1:]):
            if all([can_pass(*p1,*p2,*dp,d) for dp in def_ps]):
                graph[i].append(atk_ps.index(p2))
    
    if can_score(graph,0,l-1):
        return True
    return False
