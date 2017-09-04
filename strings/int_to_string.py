#a function that convert int to string
def int_to_string(x):
    is_negative = False
    if x <0:
        x, is_negative = -x, True
    s=[]
    while True:
        s.append(chr(ord('0')+ x%10))
        x //=10
        if x==0:
            break

    #add negative sign
    return('-' if is_negative else '')+''.join(reversed(s))
print(int_to_string(321))
