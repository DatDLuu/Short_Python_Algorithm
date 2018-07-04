# friendly reminder to msg that was not replied in >= 2days
def messageReminder(sender, receiver, dates):
    from datetime import datetime,timedelta
    num_msg = len(dates)
    
    def getDate(d,t):
        curr_dt = datetime(d[0],d[1],d[2],t[0],t[1],t[2])
        return curr_dt
    
    msg = []
    for index,item in enumerate(dates):
        x,y = item.split()
        remind_date = getDate(list(map(int,x.split('-'))),list(map(int,y.split(':'))))
        msg.append([remind_date,receiver[index],sender[index]])
    
    msg.sort()
    result = []
    pos = 0
    
    # Silly loops, but its 3:40am lol
    for pos in range(num_msg):
        rep_recvd = 0
        rem_date = msg[pos][0]+timedelta(days=2)
        if pos != num_msg -1:
            for item in msg[pos+1:]:
                if rem_date >= item[0] and msg[pos][1]==item[2] and msg[pos][2]==item[1]:
                    rep_recvd = 1
                    break
        if rep_recvd == 0:
            result.append(str(rem_date)+'. '+ msg[pos][1]+' please respond to '+ msg[pos][2])   
    return result
