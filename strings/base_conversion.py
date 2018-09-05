#function to perform base conversion
import string

def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base): #convert input string(from base10)
    # to b2
        result = ''
        if num_as_int == 0:
            return ''

        result += construct_from_base(num_as_int//base,base)+ string.hexdigits[num_as_int % base].upper()
            #parse elements into
            #the right character of the base
        return result

#convert input string to base 10
    num_as_int = 0
    index=len(num_as_string) -1
    for i in range(len(num_as_string)):
        num_as_int += int(num_as_string[i])*(b1**index)
        index -= 1

    result = construct_from_base(num_as_int, b2)
    return ('-' if num_as_string[0]=='-' else'')+('0' if num_as_string==0 else result)

print(convert_base('12', 10, 2))
