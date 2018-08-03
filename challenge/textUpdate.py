# a fun reverse challenge, given a string (a sentence)
# goal is to reverse half of the words in the string
# starting from the longest word

def textUpdate(t):
    # get word and their position
    c = [[i,v] for i,v in enumerate(t.split(" "))]
    
    # sort by word length
    c.sort(key=lambda x: len(x[1]),reverse=True)
    k = len(c)
    l = int(k/2) if k%2==0 else 1+int(k/2)

    # reverse word
    for i in range(l):
        s = c[i][1]
        c[i][1] = s[::-1]

    # rejoin the string
    return " ".join([item for (_,item) in sorted(c,key=lambda x: x[0])])
    
