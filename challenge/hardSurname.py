# count consecutive of consonant English alphabet in a given surname
def hardSurname(surname):
    r = 0
    t = 0
    for c in surname:
        if c in 'aeiouAEIOU':
            if t > r:
                r = t
            t = 0
        else:
            t+=1
    if t > r:
        r = t
    return r
