#an RPN notation is:
# 1. a single digit or a sequence of digits, followed by the option sign "-"
# 2. a form of A, B, o where o is x, +, -, /
# for example, 4, 5, x,1/
#RPN expression can be evaluated by: an int, or 2,3,x = (2x3= 6)

#write a program to take an RPN expression and return the evaluation of it

#we iterate through the array that has been splitted by ","
#if it's a number, add it to the result array
#if it's an operator, apply to the previous 2 numbers
# the last item will be the final result

def evaluate(RPN_expression):
    intermediate_result=[]
    DELIMITER = ','
    OPERATORS = {
        '+':lambda y, x: x+y,
        '-':lambda y, x: x-y,
        'x':lambda y, x: x*y,
        '/':lambda y, x: int(x/y)
    }
    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_result.append(OPERATORS[token](
                intermediate_result.pop(),
                intermediate_result.pop()))
            print(intermediate_result)
        else:
            intermediate_result.append(int(token))

    return intermediate_result[-1]

print(evaluate('2,3,x,2,/'))
