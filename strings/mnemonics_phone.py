#generate a corresponding characters sequence
#based on a string of digits
MAPPING = ('0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')
def mnemonics_phone(phone_number):
    def phone_mnemonics_helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                #print(partial_mnemonic,mnemonics)
                partial_mnemonic[digit]=c
                phone_mnemonics_helper(digit+1) #recursion
                #add two elements together then add to the final result

                #print(digit,c, partial_mnemonic[0],partial_mnemonic)
                #print('break')
    mnemonics, partial_mnemonic=[],[0]*len(phone_number)
    phone_mnemonics_helper(0)

    return mnemonics
print(mnemonics_phone('23'))
