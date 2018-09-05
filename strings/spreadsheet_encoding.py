#convert a spreadsheet column into an int
# essentially convert string into int base 26
def spreadsheet_encoding(column_name):
    index = 0
    result = 0
    for i in (reversed(range(len(column_name)))):
        result += (ord(column_name[i])-ord('A')+1) * (26**index)
        # since column A is 1 -> increment for next column
        index += 1
        print(result)
    return result
print(spreadsheet_encoding('AAA'))
  
