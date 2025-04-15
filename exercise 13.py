pi = 3.1415     # this assigns the value 3.1415 to the variable pi.
print(f"{pi}")              # this prints the value of the variable pi without any formatting. It will print "3.1415".
print(f"{pi:.3f}")          # this prints the value of the variable pi with a precision of 3 decimal places. It will print "3.142".
print(f"{pi:.10f}")         # this prints the value of the variable pi with a precision of 10 decimal places. It will print "3.1415926536".

title = " Ilocos Sur Polytechnic State College "        # this assigns the string " Ilocos Sur Polytechnic State College " to the variable title.
print(f"{title:*<80}")              # this prints the value of the variable title with a width of 80 characters. It will print " Ilocos Sur Polytechnic State College ".
print(f"{title:*^80}")              # this prints the value of the variable title with a width of 80 characters. It will print "********** Ilocos Sur Polytechnic State College **********".
print(f"{title:*>80}")              # this prints the value of the variable title with a width of 80 characters. It will print "********** Ilocos Sur Polytechnic State College ".

"""Output:

3.1415
3.142
3.1415926536
 Ilocos Sur Polytechnic State College 
 Ilocos Sur Polytechnic State College 
********** Ilocos Sur Polytechnic State College **********
********** Ilocos Sur Polytechnic State College 
"""