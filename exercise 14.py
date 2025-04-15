# data type: tuple

heroes = ("Jose Rizal", "Andres Bonifacio", "Cardo Dalisay")         # initializes a tuple named heroes. The tuple contains the values "Jose Rizal", "Andres Bonifacio", and "Cardo Dalisay".

print(heroes)       # prints the tuple. The tuple contains the values "Jose Rizal", "Andres Bonifacio", and "Cardo Dalisay".
print(type(heroes))     # prints the type of the tuple. The type of the tuple is tuple.
print(len(heroes))      # prints the length of the tuple. The length of the tuple is 3.
print(heroes[1])        # prints the second element in the tuple. The second element is "Andres Bonifacio".

heroes = list(heroes)       # converts the tuple to a list. The list contains the values "Jose Rizal", "Andres Bonifacio", and "Cardo Dalisay".

"""Output:

('Jose Rizal', 'Andres Bonifacio', 'Cardo Dalisay')
<class 'tuple'>
3
Andres Bonifacio
"""