# data type: list

fruits = ["Banana", "Starfruit", "Strawberry", "Lemon", "Kiwi"]     # initializes a list named fruits. The list contains the values "Banana", "Starfruit", "Strawberry", "Lemon", and "Kiwi".

for fruit in fruits:        # each item in the fruits list, the loop will execute the code block indented below it. In each iteration, the current item from the list will be assigned to the variable fruit.
    print("I like " + fruit)        # prints the string "I like " followed by the value of the variable fruit

"""Output

I like Banana
I like Starfruit
I like Strawberry
I like Lemon
I like Kiwi
"""