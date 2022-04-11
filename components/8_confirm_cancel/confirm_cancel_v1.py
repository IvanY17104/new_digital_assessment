print ("Please confirm your order")
print ("To confirm please enter 1")
print ("To cancel please enter 2")#Asks the users what they want

while True:#this creates a loop, so things are repeated if there are needed
    try:
        confirm = int(input("Please enter a number "))#asks the user to input which they want selected
        
        if confirm >= 1 and confirm <= 2:

            if confirm == 1:
                print("Your Order has been Confirmed and sent to the kitchen.")#if 1 is inputted it prints order confirmed
                break#breaks loop

            elif confirm == 2:
                print("Your Order has been Cancelled, you may restart your order or exit the bot")#if 2 is inputted it prints order cancelled 
                break#breaks loop
        else:
            print("The number must be 1 or 2")#prints this when a number is less than 1 or greater than 2 

    except ValueError:
        print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted