#a function to simultaneously find min and max in an array
MinMax = collections.namedtuple('MinMax',('smallest','largest'))
def find_min_max(A):
    def min_max(a,b):
        return MinMax(a,b) if a<b else MinMax(b,a)
    if len(A)<=1:
        return MinMax(A[0],A[0])

    global_min_max = min_max(A[0], A[i+1])
    #process 2 elements at a time
    for i in range(2, len(A)-1, 2): #i is the index
        local_min_max = min_max(A[i],A[i+1])
        global_min_max = (
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))

    #if there's an odd number of elements in the array
    if len(A)%2:
        global_min_max=
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1]))
    return global_min_max

#time complexity is O(n) and space complexity is O(1)
