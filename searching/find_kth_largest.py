#To find k-th largest element in the array
#since sorting is too time consuming and wasteful, we don't sorting
# use the pivot to partition the array into 2 subarrays to reduce
#the number of elements o iterate into 2
import random
import operator

def find_kth_largest(k,A):
    def find_kth(comp):
        #partition A[left:right+1] into
        #A[left:new_indx] -> > than pivot
        #and A[new_ind+1:right+1] < than pivot
        #return new_pivot_index
        def partition_around_pivot(left, right, pivot_id):
            pivot_value = A[pivot_id]
            new_pivot_index = left
            A[pivot_id],A[right]=A[right], A[pivot_id]
            for i in range(left, right):
                if A[i]<pivot_value:
                    A[i],A[new_pivot_index]=A[new_pivot_index],A[i]
                    new_pivot_index += 1

            A[right],A[new_pivot_index] = A[new_pivot_index], A[right]
            return new_pivot_index

        left, right = 0, len(A)-1
        while left <= right:
            #generates a random int in [left, right]
            pivot_id=random.randint(left, right)
            new_pivot_index = partition_around_pivot(left, right, pivot_id)
            if new_pivot_index == k-1:
                return A[new_pivot_index]
            elif new_pivot_index < k-1:
                left = new_pivot_index+1
            else:
                right=new_pivot_index -1

    return find_kth(operator.gt)
