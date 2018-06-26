# given array of int find the longest zigzag seq
# element either strictly less or greater than neighbors
# for example: 4 2 3 1 5 3

def zigzag(arr):
    max_elem = len(arr)
    if max_elem==1:
        return 1
    curr_pos = 0

    # recursive function to get length of a zigzag seq
    # given a starting pos
    def zzLength(seq,pos,grt,lsr):
        if pos==max_elem-1:
            return 1
        if grt:
            if seq[pos]<seq[pos+1]:
                return 1+zzLength(seq,pos+1,0,1)
            else:
                return 1
        if lsr:
            if seq[pos] > seq[pos+1]:
                return 1+zzLength(seq,pos+1,1,0)
            else:
                return 1

    max_zz_len = 0

    while(curr_pos<max_elem-1):
        curr_zz_len = 0
        if arr[curr_pos]>arr[curr_pos+1]:
            curr_zz_len = 1 + zzLength(arr,curr_pos+1,1,0)
            curr_pos+=(curr_zz_len-1)
        elif arr[curr_pos] < arr[curr_pos+1]:
            curr_zz_len = 1 + zzLength(arr,curr_pos+1,0,1)
            curr_pos+=(curr_zz_len-1)
        else:
            curr_zz_len=1
            curr_pos+=1

        if curr_zz_len>max_zz_len:
            max_zz_len=curr_zz_len

    return max_zz_len

