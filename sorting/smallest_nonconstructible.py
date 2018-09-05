#given a bag of change, find the smallest amount of money that these changes
# can't make up

#if an additional change is add, and its value is > A[i-1], then check
#the change can't add up to the sum of A[i-1]+1

def smallest_nonconstructible(A):
    smallest = 0
    B=sorted(A)
    for i in B:
        if i>smallest+1:
            break
        smallest += i
    return smallest+1

    #Due to the sorted method, time complexity is O(nlogn)
