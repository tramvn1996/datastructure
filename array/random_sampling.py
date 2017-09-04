#a program that generate a random sample size k from array A
import random
def random_sample(k, A):
    for i in range(k):
        r= random.randint(i, len(A)-1)
        A[i], A[r]=A[r], A[i]
    return A[:k]
print(random_sample(3,[2,3,1,4]))

#generate each element randomly and add it to the next location in the array
