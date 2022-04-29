question = "Enter your name "  # test question

while True:
    response = input(question)
    # response allows input and runs question that prints
    x = response.isalpha()
    # isalpha checks if something is in the alphabet
    # x checks if the input is something in the the alphabet
    if x == False:
        print("Input must only contain letters")
        #if x wasn't in the alphabet prints this
    else:
        print (response.title())
        break
        #if x is in the alphabet this prints and ends loop