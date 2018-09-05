#delete duplicated elements in a sorted array
def delete_duplicated(A):
    if not A:
        return 0

    write_index = 1 #start writing at index 1 to compare with index 0
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return A

B=[0,0,1,2,2,3,1]
print(delete_duplicated(B))
