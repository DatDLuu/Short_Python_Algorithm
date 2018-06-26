# python2/3 solution for alternatingKeys challenge
# code looks ugly with all the if/else
# but it works and the idea is readable

def alternatingKeys(text):
    left_hand = {key for key in "qwertasdfgzxcvb"}

    current_hand = 0
    total = 0

    for key in text:
        if key in left_hand:
            if current_hand == -1:
                total += 25
            current_hand = -1
            total += 50
        elif key == ' ':
            total += 50
            if current_hand == 1:
                current_hand = -1
            elif current_hand == -1:
                current_hand = 1
            else:
                current_hand = 0
        else:
            if current_hand == 1:
                total += 25
            current_hand = 1
            total += 50
    return total
