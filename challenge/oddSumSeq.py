# given an array of integer, if we keep replace the
# item at i-th position by the sum of all the odd integers
# before it, we will soon see the result repeating itself

'''
   [2, 5, 3, 8, 1]
   [0, 5, 8, 8, 9]
   [0, 5, 5, 5, 14]
   [0, 5, 10, 15, 15]
   [0, 5, 5, 20, 35]
   [0, 5, 10, 10, 45]
   [0, 5, 5, 5, 50]
   [0, 5, 10, 15, 15]
'''

def oddSumSequence(arr):
    rep = dict()
    step = 0

    while True:
        # record seen sequence
        rep[tuple(arr)]=step

        # generating new seq based on rule
        sum = 0
        for i,v in enumerate(arr):
            if not arr[i]%2 == 0:
                sum+=arr[i]
            arr[i]=sum

	# return first seen of the repeating seq
        step+=1
        if tuple(arr) in rep:
            return rep[tuple(arr)]
