# unpacking 

# initializes a list named numbers. The list contains a list of tuples. Each tuple contains a string and an integer.
numbers = [
    ["one", 1],
    ["two", 2],
    ["three", 3],
]

template = "The text \"{}\" is equal to {}"     # initializes a string variable named template. The string contains a placeholder for the text and the value.
for number in numbers:      # iterates through each tuple in the numbers list. In each iteration, the current tuple from the list will be assigned to the variable number.
    text = number [0]       # assigns the first element of the tuple to the variable text.
    value = number [1]      # assigns the second element of the tuple to the variable value.
    
    output = template.format (text, value)      # formats the string template with the values of text and value.
    print(output)           # prints the formatted string.

print("========")            # prints a separator line.

#[]"three", 3]
for number in numbers:
    text, value = number        # unpacks the tuple number into two variables: text and value. The first element of the tuple is assigned to the variable text, and the second element is assigned to the variable value.
    
    output = template.format (text, value)
    print(output)

    print("========")


for text, value in numbers:     # a third for loop that directly unpacks the inner lists in the numbers list. The first element of each inner list is assigned to the variable text, and the second element is assigned to the variable value.
        
    output = template.format (text, value)
    print(output)


"""Output:

The text "one" is equal to 1
The text "two" is equal to 2
The text "three" is equal to 3
========
The text "one" is equal to 1
========
The text "two" is equal to 2
========
The text "three" is equal to 3
========
The text "one" is equal to 1
The text "two" is equal to 2
The text "three" is equal to 3
"""
