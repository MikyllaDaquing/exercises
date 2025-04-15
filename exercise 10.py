#DRY: Don't Repeat Yourself

age = int(input("How old are you? "))   # prompts the user to enter their age using the input() function. The input is then converted to an integer using the int() function


if age >= 80 or age <= 0:           # checks if the age is greater than or equal to 80 or less than or equal to 0
    print("That is not a valid age")        # prints the message "That is not a valid age"

elif age >= 18:                     # checks if the age is greater than or equal to 18
    print("You can drive! ")                # prints the message "You can drive!"

else:                               # if the age is less than 18.
    print("You cannot drive yet")               # prints the message "You cannot drive yet"
    print("Wait a few years")               # prints the message "Wait a few years"

"""Output

How old are you? 15
You cannot drive yet
Wait a few years
"""