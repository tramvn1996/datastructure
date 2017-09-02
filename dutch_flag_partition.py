#the dutch flag problem
#partition an array according to a pivot point 
#(all elements before the pivot point have to be smaller than it, and the elements after have to be smaller

def dutch_flag_parition(pivot_index, A)
    pivot = A[pivot_index]
    #keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group A[equal:larger]
    # top group: A[larger:]
    
    smaller, equal, larger = 0, 0, len(A)
    #keep iterating as long as there is an unclassified element
    
    while equal < larger:
      #A[equal] is the incoming unclassified element
      if A[equal] < pivot:
        A[smaller], A[equal] = A[equal], A[smaller]
        smaller, equal = smaller +1 , equal + 1
      elif A[equal] == pivot:
        equal += 1
      else: #A[equal] > pivot
        larger -= 1
        A[equal], A[larger] = A[larger], A[equal]
        
        #time complexity is O(n), space complexity O(1)

#Another approach
def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1
            
