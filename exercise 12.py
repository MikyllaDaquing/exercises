#while loop

while True:     #this will loop forever.
    
    reply = input("Totoo ba? ").lower()     # this will prompt the user to enter a response and convert it to lowercase. The input is then assigned to the variable reply.
    if reply in ["yes", "oo", "opo"]:       # this checks if the value of the variable reply is one of the strings "yes", "oo", or "opo". If it is, the code block indented below it will execute.
        break                               # this breaks out of the loop. The loop will stop executing when this line is reached.

    if reply == "hinde":                    # this checks if the value of the variable reply is the string "hinde". If it is, the code block indented below it will execute.
        print("liar")                       # this prints the string "liar".
        continue                            # this continues to the next iteration of the loop.

    print("Let's go again ")                # this prints the string "Let's go again ".

print("Tapos ang usapan")                   # this prints the string "Tapos ang usapan".

"""Output

Totoo ba? hinde
liar
Let's go again 
Totoo ba? yes
Tapos ang usapan
"""