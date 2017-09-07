#look and say
#for example 1 (There's one 1) -> 11 (There's two 1's) -> 21

def look_and_say(n):
    def next_number(s):
        result , i = [], 0
        while i < len(s):
            count = 1
            while i+1 <len(s) and s[i]==s[i+1]:
                i += 1
                count += 1
            result.append(str(count)+s[i])
            i+=1
        return ''.join(result) #function to join string together instead of array form
    s='1'
    for _ in range(1, n):
        s=next_number(s)
    return s

print(look_and_say(6))

#time complexity O(n2^n)
#since the next number is always twice the previous one
#and each iteration, we have to loop through n times
