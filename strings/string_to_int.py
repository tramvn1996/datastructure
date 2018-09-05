#convert string to int
import functools
import string

def string_to_int(s):
    result=0
    index = len(s)-1
    for i in range(len(s)):
        result += string.digits.index(s[i]) * (10**index)
        index -= 1
        print(result) #try to see result after each loop

    return result
print(string_to_int("234"))
