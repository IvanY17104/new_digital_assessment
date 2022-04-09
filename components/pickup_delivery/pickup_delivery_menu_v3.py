#menu so that user can choose either pickup or delivery

print ("Do you want your order delivered or are you picking it up?")
print ("For delivery enter 1")
print ("For pickup enter 2")#Asks the users what they want

delivery = int(input())#Makes delivery an integer (number) input

if delivery == 1:
    print("Delivery")#If 1 is inputted it prints delivery

elif delivery == 2:
    print("Pickup")#If 2 is inputted it prints pickup

else:
    print("That was not a valid input")#If 1 or 2 isnt inputted it prints this




