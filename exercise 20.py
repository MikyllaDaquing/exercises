#open(filename,mode)

f = open("hello.txt", "a")      # open the file hello.txt in append mode.
f.write("Hello World \n")       # write the string "Hello World" to the file hello.txt
f.write("Apple \n")             # write the string "Apple" to the file hello.txt
f.write("Banana \n")            # write the string "Banana" to the file hello.txt
f.write("Strawberry \n")        # write the string "Strawberry" to the file hello.txt
f.write("Dalandan \n")          # write the string "Dalandan" to the file hello.txt
f.close()                       # close the file

with open("hello.txt", "a") as f:       # open the file hello.txt in append mode.
    f.write("Good afternoon\n")         # write the string "Good afternoon" to the file hello.txt
    f.write("\n")                       # write a newline character to the file hello.txt