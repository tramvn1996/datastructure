#function to find intersection of 2 sorted array
#
def intersection_two_sorted_arrays(A,B):
    i, j, intersection_A_B=0,0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i==0 or A[i]!=A[i-1]:
                intersection_A_B.append(A[i])
            i, j = i+1, j+1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B
# we spend O(1) time per input array element, the time for the entire algo is
#O(m+n)
