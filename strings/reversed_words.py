#reverse all words in an array
#assume s is a string encoded as bytearray

def reverse_words(s):
    s.reverse()

    def reverse_range(s, smart, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start+1, end-1

    start = 0
    while True:
        end=s.find('',start)
        if end < 0:
            break

            reverse_range(s, smart, end-1)
            start = end+1
    reverse_range(s, smart, len(s)-1)

print(reverse_words('Bi ba bi bo'))
#string.find(s, sub[, start[, end]])
#Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.
