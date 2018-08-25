# given list of integers arr and a max value
# find value i such that 1 <= i <= max
# and range(i,arr[j]) is the biggest
# 	for arr[j-1] < i < arr[j]
# 	for j in range(len(arr))

def comeOnDown(maxPrice, bids):
    prop=chances=0
    for bid in sorted(bids+[maxPrice+1]):
        if maxPrice > prop < bid-chances:
            chances = bid-prop
            result = prop+1
        
        prop = bid
    return result
