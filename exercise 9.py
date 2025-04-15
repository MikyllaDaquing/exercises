#list comprehension
fruits = ["Banana", "Starfruit", "Strawberry"]      # initializes a list named fruits. The list contains the values "Banana", "Starfruit", and "Strawberry".

fruits2 = []        # initializes an empty list named fruits2.

#for fruit in fruits:
 #   fruits2.append(fruit.upper())

fruits2 = [fruit.upper() for fruit in fruits]       # this creates a new list named fruits2 by converting each element in the fruits list to uppercase using a list comprehension.

print(fruits2)      # prints the fruits2 list

"""Output:

['BANANA', 'STARFRUIT', 'STRAWBERRY']"""