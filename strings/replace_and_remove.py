#apply 2 rules to an array of characters
## replace 'a' with 'dd'
## remove all 'b's

#implement by looping through the array once to count 'a'
# and remove 'b' by skipping over it in the counter point
# come up with the length of the new array depend on how many 'a's there are

#then go back and arrange elements

def replace_and_remove(size, s):
    #size indicate whether we want to apply this to the entire array or not

    #first loop, remove b and count a
    write_index, a_count=0,0
    for i in range(size):
        if s[i]!='b':
            s[write_index]=s[i]
            write_index += 1
        if s[i]=='a':
            a_count += 1

    #2nd loop, replace and reaarange array
    current_index = write_index - 1 #start loop from the very back
    write_index += a_count - 1 #add the 'a' and -1 since it's index
    final_size=write_index + 1

    while current_index >= 0:
        if s[current_index] == 'a':
            s[write_index-1 : write_index+1]='dd'
            write_index -= 2
        else: #move non-'a' to the right to get space for dd
            s[write_index] = s[current_index]
            write_index -= 1
        current_index -= 1

    return final_size, s

print(replace_and_remove(4, ['a','c','a','a']))
