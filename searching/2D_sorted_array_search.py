#2D sorted array is an array whose elements appear in non-decreasing order
#write a function that checked if the input integer is in the 2D array

#since the 2D array is sorted (m rows and n cols), if
# x > A[0][n-1] -> x is greater than all elements in rows 0
# x < A[0][n-1] -> x is smaller than all elements in col n-1

def matrix_search(A,x):
    row, col = 0, len(A[0])-1 #start from the upper left corner
    while row < len(A) and col >= 0:
        if A[row][col]==x:
            return True
        elif A[row][col] > x:
            col -= 1
        else:
            row += 1
    return False

#since we iterate through m+n-1 elements, time complexity is O(m+n-1)
