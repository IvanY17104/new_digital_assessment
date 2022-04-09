customer_details = {}#a dictionary to store customer details

def not_blank(question):#a not blank function to check if something isnt blank
    valid = False
    while not valid:#a loop
        response = input(question)#asks the question that is stated, and allows input
        if response != "":
            return response#if input isn't blank returns it back
        else:
            print("Sorry this cannot be blank")#if input is blank this is printed



question = ("Please enter your name ")#asks the user to enter their name
customer_details['name'] =  not_blank(question)#customer_details goes off to not_blank, later not_blank is sent back to customer_details after input
print(customer_details['name'])#prints input

question = ("Please enter your phone number ")#asks the user to enter theirn phone number
customer_details['phone'] = not_blank(question)#same as above
print(customer_details['phone'])#prints input

question = ("Please enter your house number ")#asks the user for their house number and allows input
customer_details['house'] = not_blank(question)
print(customer_details['house'])
#prints input

question = ("Please enter your street name ")#asks the user for their street name and allows input
customer_details['street'] = not_blank(question)
print(customer_details['street'])#prints input

question = ("Please enter your suburb ")#asks the user for their suburb and allows input
customer_details['suburb'] = not_blank(question)
print(customer_details['suburb'])#prints input


