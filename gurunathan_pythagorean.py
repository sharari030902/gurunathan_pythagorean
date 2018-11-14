x = raw_input ("Name:")
print ("Welcome, " + x)
from math import sqrt
 
# Defining varibles and taking input from user
A = raw_input ("Enter 1st side:")
B = raw_input ("Enter 2nd side:")
 
#
ASQU = int(A) * int(A)
BSQU = int(B) * int(B)
AandB = int(ASQU)+int(BSQU)
answer = sqrt(AandB)
print "The length of side C is" + str(answer)