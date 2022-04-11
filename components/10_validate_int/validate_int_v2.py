def order_type(low, high, question):
    while True:#this creates a loop, so things are repeated if there are 
            try:
                num = int(input(question))
                if num >= low and num <= high:
                    return num#if the number is an appropriote number between what we need it returns it
                else:
                    print(f"The number must be between {low} or {high}")#prints this when a number that we didn't want is inputted

            except ValueError:
                print(f"That is not a valid number, please enter a number between {low} and {high}")#this prints when numbers arent inputted

low = 1
high = 2#test data

question = (f"Please enter a number between {low} and {high} ")#test question

answer = order_type(low, high, question)

print(answer)