#a program that return the next permutation
# essentially, find the smallest permutation that's larger than the orgiginal one
# we do this by identifying where in the array that elements start decreasing

def next_permutation(perm):
    #find the first entry from the right
    #that is smaller than the entry right after it

    inversion_point = len(A)-2
    while (inversion_point>=0 and perm[inversion_point]>=perm[inversion_point+1]):
        inversion_point -= 1
    if inversion_point == -1:
        return [] #perm is the last permutation
    for i in reversed(range(inversion_point+1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i]=perm[i], perm[inversion_point]
            break
            #exchange with the larger value in the furthest right as possible
            #to the inversion_point

#entries in perm must appear in decreasing order after inversion_point
#to yield smallest permutation, so we reversed the order
    perm[inversion_point+1:]=reversed(perm[inversion_point+1:])
    return perm
