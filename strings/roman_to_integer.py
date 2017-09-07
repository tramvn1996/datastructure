#a function to convert roman to decimal
def roman_to_integer(s):
    mapping = {'I': 1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = mapping[s[-1]]

    for i in reversed(range(1,len(s))):
        if mapping[s[i]]>mapping[s[i-1]]:
            result -= mapping[s[i-1]]
        else:
            result += mapping[s[i-1]]
    return result

print(roman_to_integer('XXI'))
