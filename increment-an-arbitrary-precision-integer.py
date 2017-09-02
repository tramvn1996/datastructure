# Write a program that takes an array encoding a nonnegative decimal integer D, 
# and update the array to represent the integer D+1
def plus_one(A):
    A[-1] += 1 
    for i in reversed(range(1,len(A)):
        if A[i] != 10:
            break #if the last digit is not 10, then the new array is set
     # otherwise, need to update the carry-on 
        A[i] = 0
        A[i - 1]  += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
