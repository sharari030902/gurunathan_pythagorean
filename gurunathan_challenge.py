from math import sqrt
 
# Defining varibles and taking input from user
Leg1 = raw_input ("Enter 1st side:")
Leg2 = raw_input ("Enter 2nd side:")
Leg3 = raw_input ("Enter 3rd side:")
 
#Squaring values
legOneSq = int(Leg1) * int(Leg1)
legTwoSq = int(Leg2) * int(Leg2)
legThreeSq = int(Leg3) * int (Leg3)
 
Total_legOneandTwo = int(legOneSq)+int(legTwoSq)
 
if int(Leg1)+int(Leg2) < int(Leg3):
    print "This is not a triangle..."
elif Total_legOneandTwo == int(legThreeSq):
    print "This is a right triangle..."
elif Total_legOneandTwo < int(legThreeSq):
    print "This ia Obtubse triangle..."
elif Total_legOneandTwo > int(legThreeSq):
    print "This is a actute triangle..."