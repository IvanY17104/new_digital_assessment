#bug -  need to make it so that it only accepts 1 or 2

#menu so that user can choose either pickup or delivery

print ("Do you want your order delivered or are you picking it up?")
print ("For delivery enter 1")
print ("For pickup enter 2")#Asks the users what they want

low = 1#lowest number user can input is 1
high = 2#highest number user can input is 2

while True:#this creates a loop, so things are repeated if there are 
    try:
        delivery = int(input("Please enter a number"))#delivery allows integer inputs
        
        if delivery == 1:
            print("Delivery")#if 1 is inputted it prints delivery
            break#breaks loop

        elif delivery == 2:
            print("Pickup")#if 2 is inputted it prints pickup
            break#breaks loop

    except ValueError:
        print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted




