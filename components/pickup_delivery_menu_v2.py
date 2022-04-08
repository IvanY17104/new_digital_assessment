#Bugs
#Will only work for valid input "d" and "p"
#invalid input triggers else statement but program is not asking for input again

#menu so that user can choose either pickup or delivery

print ("Do you want your order delivered or are you picking it up?")
print ("For delivery enter d")
print ("For pickup enter p")#Asks users what they want

delivery = input()#Makes "Delivery" an input

if delivery == "d":
    print("Delivery")#If d is inputted it prints delivery

elif delivery == "p":
    print("Pickup")#If p is inputted it prints pickup

else:
    print("That was not a valid input")#If d or p isnt inputted it prints this




