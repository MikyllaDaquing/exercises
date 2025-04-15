# string formatting operator

name = input ("What is your name: ")        # this prompts the user with "What is your name: " and waits for their input. The input is then assigned to the variable name
age = int(input("How old are you? "))       # this prompts the user with "How old are you? " and waits for their input. The input is then converted to an integer using the int() function

output = "You are %s. You are %i years old" % (name,age)    # this assigns the string "You are %s. You are %i years old" to the variable output. The %s and %i placeholders are replaced with the values of name and age.

output = "You are {}. You are {} years old ".format(name,age)    # this assigns the string "You are {}. You are {} years old " to the variable output. The {} placeholders are replaced with the values of name and age.

output = f"You are {name}. You are {age} years old "    # this assigns the string "You are {name}. You are {age} years old " to the variable output. The {name} and {age} placeholders are replaced with the values of name and age.

print(output)   # this prints the value of the variable output

"""Output

What is your name: princess
How old are you? 15
You are princess. You are 15 years old
You are princess. You are 15 years old
You are princess. You are 15 years old
"""