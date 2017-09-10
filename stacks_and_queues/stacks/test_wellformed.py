#test if a string is well formed meaning
# for every open bracket, there's one to close it

def test_wellformed(s):
    left_char, lookup = [], {'(':')', '[':']', '{':'}'}
    for i in s:
        if i in lookup:
            left_char.append(i)
            print(i)
        elif not left_char or i != lookup[left_char.pop()] :
            print(i)
            return False
    return not left_char

print(test_wellformed('(()'))
