#write a program that takes 2 arrays and return their product
def multiply(num1, num2):
    if num1[0] < 0 or num2[0] < 0:
        sign = -1
    else:
        sign = 1
    result = [0] * (len(num1) + len(num2))

#multiply
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i +j] += result[i + j + 1]//10
            result[i+j+1] %= 10

#remove leading zeroes
    while result[0] == 0:
        result = result[1:]

    return [sign*result[0]]+result[1:]

A=[1,2]
B=[1,2]
print(multiply(A,B))
