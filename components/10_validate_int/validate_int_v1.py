def order_type():
    while True:#this creates a loop, so things are repeated if there are 
            try:
                num = int(input())
                if num >= 1 and num <= 2:
                    return num
                else:
                    print("The number must be 1 or 2")#prints this when a number is less than 1 or greater than 2 

            except ValueError:
                print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted

print("Please enter a number between 1 and 2")

answer = order_type()

print(answer)