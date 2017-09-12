#write a function that computes the real square root
def real_sq_root(x):
    #decide search range
    left, right = (x,1.0) if x < 1 else (1.0, x)

    #keeps searching as long as left!=right
    while not math.isclose(left, right):
        mid = (left+right) * 0.5
        mid_square = mid * mid
        if mid_squre > x:
            right = mid
        else:
            left = mid

    return left
    
