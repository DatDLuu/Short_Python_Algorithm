# given a string represents rock paper scissor moves
# calculate corresponding moves based on rules
'''the rules you'll be following:

If you win, switch to what your opponent played
If you lose, switch to whatever wasn't played that round
In case of a draw, choose the move you've played least frequently
If there's a tie among these, choose the one you've played most recently
If there's a draw on the first move, choose Rock next
Always start with Scissors (you've heard it's statistically most likely to win)
'''
# return [win,lose,draw] based on calculated moves

def rockPaperScissor(opponentsMoves):
    result = [0,0,0]
    move = "S"
    point = {"R":[0,-1,1],"P":[1,0,-1],"S":[-1,1,0]}
    moves_index = {"R":0,"P":1,"S":2}
    played = {"R":0,"P":0,"S":0}
    
    most_rec = sec_most = ""
    
    
    for index,opp_move in enumerate(opponentsMoves):
        m_i = moves_index[opp_move]
        p = point[move][m_i]
        played[move]+=1
        
        if most_rec != move:
            sec_most = most_rec
            most_rec = move
        
        if p == 1:
            move = opp_move
            result[0]+=1
            continue
            
        if p == -1:
            temp = ["R","P","S"]
            temp.remove(move)
            temp.remove(opp_move)
            move = temp[0]
            result[1]+=1
            continue
        if p == 0:    
            result[2]+=1
            if index == 0:
                move = "R"
                continue
            else:
                least_chose = [i for i in played if played[i]==min(played.values())]
                if len(least_chose) > 1:
                    if most_rec in least_chose:
                        move = most_rec
                        continue
                    if sec_most in least_chose:
                        move = sec_most
                        continue
                else:
                    move = least_chose[0]
                    continue
    return result
