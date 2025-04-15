#string methods

sentence = "The quick brown Fox jumps over the lazy Dog"    # initializes a string variable named sentence with the value "The quick brown Fox jumps over the lazy Dog".

print(sentence.upper())     # print the sentence in upper case. The first letter of each word is uppercase.
print(sentence.lower())     # print the sentence in lower case. The first letter of each word is lowercase.
print(sentence.title())     # print the sentence in title case. The first letter of each word is capitalized.
print(sentence.swapcase())      # print the sentence in swapcase. The first letter of each word is swapped between uppercase and lowercase.

#sentence = sentence.upper()

sentence = sentence.replace("Fox", "elephant")      # replaces the word "Fox" with the word "elephant". 

print(sentence)     # print the sentence

"""Output:

THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
the quick brown fox jumps over the lazy dog
The Quick Brown Fox Jumps Over The Lazy Dog
tHE qUICK bROWN fOX jUMPS oVER tHE lAZY dOG
The quick brown elephant jumps over the lazy dog"""