# test if a string can be permutated so that it'll become palindrome
# condition:
#if len(s) is odd -> 1 element need appear an odd number of times
# if len(s) is even -> all elements need to appear an even number of times
import collections

def can_string_be_a_palindrome(s):
    return sum(v%2 for v in collections.Counter(s).values()) <= 1
#time O(n) n-length of the string
#space O(c) c-> number of distinct character in the string
