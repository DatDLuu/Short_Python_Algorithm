# another fun challenge of concatenate string
# given list of string s (road sign), the result string will be
# first word in s[0] + first word in s[1] + ... + second word in s[0] + second word in s[1] + ...
# til we dont have anything to concatenate
# rules: word separate by " " left and right, except first word, punctuation "!?." doesnt have left " "
#	 upper case first char in word if: punc, word ended with punc
#	 lower case everything else

def roadSigns(sign):
    import itertools
    # upper case first char and lower the rest
    cap_up = lambda x: x[0].upper()+x[1:].lower()

    c = itertools.zip_longest(*[i.split(" ") for i in sign],fillvalue='-')
    r = ""
    punc = ['!','?','.']

    cap = True
    for item in c:
        for word in item:
            if word == '-':
                continue
            
            if word in punc and len(word)==1:
                cap = True
                r+=word
                continue
                
            if cap:
                r+=(" "+cap_up(word))
                cap = True
            else:
                r+=(" "+word.lower())
                
            cap = True if word[-1] in punc else False
        
    return r[1:]
