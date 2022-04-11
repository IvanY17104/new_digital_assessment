print ("Do you want to create another order or exit?")
print ("To order please enter 1")
print ("To exit please enter 2")#Asks the users what they want

while True:#this creates a loop, so things are repeated if there are needed
    try:
        confirm = int(input("Please enter a number "))#asks the user to input which they want selected
        
        if confirm >= 1 and confirm <= 2:

            if confirm == 1:
                print("Another order will be created")#if 1 is inputted it prints another order will be created
                break#breaks loop

            elif confirm == 2:
                print("You will be exited from the bot")#if 2 is inputted it prints you will be exited from bot 
                break#breaks loop
        else:
            print("The number must be 1 or 2")#prints this when a number is less than 1 or greater than 2 

    except ValueError:
        print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted