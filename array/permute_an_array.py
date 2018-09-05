#a program that reorder an array based on a sample array
def permute_array(perm, A):
    #since we subtract every elements of perm
    # so that every elements that has been applied will be negative

    #we check if it's negative first
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i],A[perm[next]]= A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
            print(A,perm)
            #restore perm
    #for j in range(len(perm)):
        #perm[j] += len(perm)
    return A, perm

A=['a','b','c','d']
perm=[3,2,1,0]
print(permute_array(perm, A))
