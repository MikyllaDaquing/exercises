numbers = [1,2,3,4,5,6,7,8,9,10]        # initializes a list named numbers. The list contains the values 1 through 10.
evens = []                              # initializes an empty list named evens.

for number in numbers:      # iterates through each element in the numbers list. In each iteration, the current element from the list will be assigned to the variable number.
    if number % 2 == 0:         # checks if the value of the variable number is divisible by 2. If it is divisible, the code block indented below it will execute.
        evens.append(number)        # adds the value of the variable number to the evens list. This is done by calling the append() method on the evens list and passing in the value of the variable number as an argument.

#evens = [numbers for number in numbers if number % 2 == 0]

evens = [
    number for number in numbers        # this creates a new list named evens by iterating through each element in the numbers list. In each iteration, the current element from the list will be assigned to the variable number.
    if number % 2 == 0                  # this checks if the value of the variable number is divisible by 2. If it is divisible, the code block indented below it will execute. 
]

print(evens)        # prints the evens list.

"""Output:

[2, 4, 6, 8, 10]"""