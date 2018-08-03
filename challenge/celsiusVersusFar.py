# given a list of temperature measured in celsius
# given a list of temperature measured in fahrenheit
# calculate how many item in F is greater than in C
# F = C*9/5 + 32

def celsiusVsFahrenheit(yourTemps, friendsTemps):
    r = 0
    for i,v in enumerate(yourTemps):
        if v*9/5+32 < friendsTemps[i]: r+=1
    return r
