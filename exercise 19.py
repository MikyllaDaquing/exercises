#open(filename,mode)

f = open("hello.txt", "w")      # open the file hello.txt in write mode.
f.write("Hello world")          # write the string "Hello world" to the file hello.txt
f.close()                       # close the file