# we want to use letters from a magazine to write an anonymous letter
# so we would want to count if the number of characters from the
#magazine can provide enough letters for our letters

#first approach:
def is_letter_contructible(letter_text, magazine_text):
    char_frequency_for_letter = collections.Counter(letter_text)

    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c]==0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True
    return not char_frequency_for_letter
    #time O(m+n) m-> length of the letter_text, n-> length of magazine_text

#second approach:
def python_is_letter_constructible(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

    #second approach takes advantage of the subtract operation for Counter
    #space O(L)-> number of distinct character in the letter_text
