# find first duplicate in a given array
# if theres none or only 1 elem return -1
def firstDuplicate(arr):
    unique=set()
    for elem in arr:
        if elem in unique:
            return elem
        unique.add(elem)
    return -1