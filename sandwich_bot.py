#Sandwich Store program

#Bugs -
#4/9/2022
# phone number input allows letters
# name input allows numbers

#Known Bugs
#Final printout is not printing customer details correctly

import random
from random import randint #this import allows me to create a random number generator
import sys#imports sys into the program

names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']
#list of sandwich names

sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]
#list of sandwich prices

order_list = []
order_cost = []#lists to store sandwich orders and costs

customer_details = {}#a dictionary to store customer details

#validates inputs to check if they are blank
def not_blank(question):#a not blank function to check if something isnt blank
    valid = False
    while not valid:#a loop
        response = input(question)#asks the question that is stated, and allows input
        if response != "":
            return response.title()#if input isn't blank returns it back, and it makes the input's first letter have capital and the rest lower case
        else:
            print("Sorry this cannot be blank")#if input is blank this is printed
            
            #validates input to check if it is an integer

def val_int(low, high, question):
    while True:#this creates a loop, so things are repeated if there are 
            try:
                num = int(input(question))
                if num >= low and num <= high:
                    return num#if the number is an appropriote number between what we need it returns it
                else:
                    print(f"The number must be between {low} or {high}")#prints this when a number that we didn't want is inputted

            except ValueError:
                print(f"That is not a valid number, please enter a number between {low} and {high}")#this prints when numbers arent inputted

#Welcome message with random name   
def welcome(): #Created a function for welcome
    '''
    Purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''

    num = randint(0,9) #num will give a random number (randint) between 0 to 9
    name = (names[num]) #each name in names has a number associated with it, and num  will give a random number, so 'name' will give a random name
    print("Welcome to Ivan's Sandwich Store!")
    print("My name is",name,"and I will help you take your Sandwich orders.") #This is the welcome message that will show up




#Menu for pickup or delivery
def order_type():
    del_pick = ""
    low = 1
    high = 2
    question = (f"Please enter a number between {low} and {high} ")#confirms low/high for this function

    print ("Do you want your order delivered or are you picking it up?")
    print ("For delivery enter 1")
    print ("For pickup enter 2")#Asks the users what they want

    delivery = val_int(low, high, question)
    if delivery == 1:
        print("Delivery")#if 1 is inputted it prints delivery
        delivery_info()#will activate delivery function and begin asking things for delivery
        del_pick = "delivery"#if delivery is picked del_pick variable becomes delivery

    else:
        print("Pickup")#if 2 is inputted it prints pickup
        pickup_info()#will activate pickup function and begin asking things for pickup
        del_pick = "pickup"#if pickup is picked del_pick variable becomes pickup

    return del_pick#returns variable back 



#Pickup information - name and phone number
def pickup_info():
    question = ("Please enter your name ")#asks the user to enter their name
    customer_details['name'] =  not_blank(question)#customer_details goes off to not_blank, later not_blank is sent back to customer_details after input
    print(customer_details['name'])#prints input

    question = ("Please enter your phone number ")#asks the user to enter theirn phone number
    customer_details['phone'] = not_blank(question)#same as above
    print(customer_details['phone'])#prints input
    
    print(customer_details)



#Delivery Infornation - name address and phone
def delivery_info():
    question = ("Please enter your name ")#asks the user to enter their name
    customer_details['name'] =  not_blank(question)#customer_details goes off to not_blank, later not_blank is sent back to customer_details after input
    print(customer_details['name'])#prints input

    question = ("Please enter your phone number ")#asks the user to enter theirn phone number
    customer_details['phone'] = not_blank(question)#same as above
    print(customer_details['phone'])#prints input

    question = ("Please enter your house number ")#asks the user for their house number and allows input
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])#prints input

    question = ("Please enter your street name ")#asks the user for their street name and allows input
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])#prints input

    question = ("Please enter your suburb ")#asks the user for their suburb and allows input
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])#prints input
    



#Sandwich Menu
def menu():
    number_sandwich = 10

    for count in range (number_sandwich):
        print("{} {} ${:.2f}" .format(count+1,sandwich_names[count], sandwich_prices[count]))
        #the 3 {} brackets contain count sandwich name and price count, so things that we do in those affect the count print
        #dollar sign and :.2f makes the sandwich prices have a dollar sign infront, and have 2 decimal places
        #count +1 makes it so that the index numbers start at 1 and not 0




#Choose total number of items - max 5 & Sandwich Ordering - from menu - print each item with cost
def order_sandwich():
    #ask for total number of sandwiches
    num_sandwiches = 0
    low = 1
    high = 5
    menu_low = 1
    menu_high = 12#the low and high values for the two things we need to validate
    question = (f"Please enter a number between {low} and {high} ")#question for first 
    print("How many sandwiches would you like to order?")
    num_sandwiches = val_int(low, high, question)#asks how many sandwiches want to be ordered, validates integers

    #choose sandwich from menu
    for item in range(num_sandwiches):
        while num_sandwiches > 0:
            print("Please choose your sandwiches by entering the number from the menu  ")
            question = (f"Please enter a number between {menu_low} and {menu_high} ")
            sandwich_ordered = val_int(menu_low, menu_high, question) #asks user to enter which pizza they want, validats integer
            sandwich_ordered = sandwich_ordered - 1#this is so that it doesn't print the wrong things since we ahve the index numbers starting at 1 instead of 0
            order_list.append(sandwich_names[sandwich_ordered])
            order_cost.append(sandwich_prices[sandwich_ordered])#the inpuuted number is then sent to the sandwich names and prices which sends back the respective index number items.
            print("{} ${:.2f}" .format(sandwich_names[sandwich_ordered],sandwich_prices[sandwich_ordered]))#prints the sandwich names and prices together, prices have a dollar sign and are 2 d.p
            num_sandwiches = num_sandwiches-1#this is what helps create the loop by taking 1 away from num_sandwiches for every one that is ordered




#Print order out - including if order is delivery or pickup and names and price of each item - total cost
def print_order(del_pick):
    total_cost = sum(order_cost)#total_cost is the sum of all prices in order_cost
    print()
    print("Customer Details")
    if del_pick == "delivery":
        print("Your order is for Delivery, there will be a $5 delivery fee applied")
        total_cost = total_cost + 5
        print(f"Name: {customer_details['name']} \nPhone: {customer_details['phone']} \nHouse Number: {customer_details['house']} \nStreet Name: {customer_details['street']} \nSuburb: {customer_details['suburb']}")
        #\n makes it go down one line, so they are all on seperate lines
    elif del_pick == "pickup":
        print("Your order is for Pickup")
        print(f"Name: {customer_details['name']} \nPhone: {customer_details['phone']}")
        #if del_pick is delivery it prints all 5 things, if del_pick is pickup it only prints the two
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
        #this prints the order list with an 'Ordered' infront of it, and order cost with 'Cost' and $ infront of it with it also being 2 d.p
        count = count + 1#the count+1 is so that after it prints one order_cost it adds one and prints the next ones
    print()
    print(f"The total cost of the order is:${total_cost:.2f}")
    print()
    #this prints out the total cost of the order properly, with a $ sign and 2 d.p



#Ability to cancel or proceed with order
def confirm_cancel():
    low = 1
    high = 2
    question = (f"Please enter a number between {low} and {high} ")#confirms the high/low for this function
    print ("Please confirm your order")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")#Asks the users what they want

    confirm = val_int(low, high, question)#validates integer
    if confirm == 1:
            print("Your Order has been Confirmed and sent to the kitchen.")#if 1 is inputted it prints order confirmed
            new_exit()
    elif confirm == 2:
            print("Your Order has been Cancelled, you may restart your order or exit the bot")#if 2 is inputted it prints order cancelled 
            new_exit()




#Create option for new order or to exit
def new_exit():
    low = 1
    high = 2
    question = (f"Please enter a number between {low} and {high} ")#confirms the high/low for this function

    print ("Do you want to create another order or exit?")
    print ("To order please enter 1")
    print ("To exit please enter 2")#Asks the users what they want
    confirm = val_int(low, high, question)#validates integer
    if confirm == 1:
        print("Another order will be created")#if 1 is inputted it prints another order will be created
        order_list.clear()
        order_cost.clear()
        customer_details.clear()#clears all inputs that were put into these lists/dictionaries
        main()#runs main again, restarting bot


    elif confirm == 2:
        print("You will be exited from the bot")#if 2 is inputted it prints you will be exited from bot 
        order_list.clear()
        order_cost.clear()
        customer_details.clear()#clears all inputs that were put into these lists/dictionaries
        sys.exit()#exits bot




#Main Funciton
def main(): #Created a function to run all the functions
    '''
    Purpose: To run all functions
    Parameters: none
    Returns: none
    '''
    welcome()
    del_pick = order_type() #del_pick is a variable that will come from order_type
    menu()
    order_sandwich()
    print_order(del_pick)#when print_order function happens the del_pick variable is sent there
    confirm_cancel()


main() #Runs the main function 


