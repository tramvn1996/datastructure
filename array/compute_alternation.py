#a program that order elements
# A[i]<A[i+1]>A[i+2]...
def compute_alternation(A):
    for i in range(len(A)):
        A[i:i+2]=sorted(A[i:i+2], reverse=i%2)

    return A

B=[1,2,3,4,5,6,7,8]
print(compute_alternation(B))
