fruits = []     # initializes an empty list named fruits. The list is empty because it does not contain any elements.
fruits.append("Apple")      # adds the string "Apple" to the end of the fruits list

#fruits[0] = "Apple"
#fruits[1] = "banana"
print(fruits)       # prints the fruits list

print("banana" not in fruits)       # prints True because the string "banana" is not in the fruits list. The "not" keyword is used to negate the result of the "in" keyword.
print("carrot" in fruits)           # prints False because the string "carrot" is not in the fruits list. The "in" keyword is used to check if a string is in the fruits list.

"""Output:

['Apple']
True
False"""