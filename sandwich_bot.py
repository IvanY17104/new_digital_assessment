#Sandwich Store program

#Bugs -
#4/9/2022
# phone number input allows letters
# name input allows numbers

import random
from random import randint #this import allows me to create a random number generator

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
    print ("Do you want your order delivered or are you picking it up?")
    print ("For delivery enter 1")
    print ("For pickup enter 2")#Asks the users what they want

    low = 1#lowest number user can input is 1
    high = 2#highest number user can input is 2

    while True:#this creates a loop, so things are repeated if there are 
        try:
            delivery = int(input("Please enter a number "))#delivery allows integer inputs
            
            if delivery >= 1 and delivery <= 2:

                if delivery == 1:
                    print("Delivery")#if 1 is inputted it prints delivery
                    delivery_info()#will activate delivery function and begin asking things for delivery
                    break#breaks loop

                elif delivery == 2:
                    print("Pickup")#if 2 is inputted it prints pickup
                    pickup_info()#will activate pickup function and begin asking things for pickup
                    break#breaks loop
            else:
                print("The number must be 1 or 2")#prints this when a number is less than 1 or greater than 2 

        except ValueError:
            print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted



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
    while True:#while num_sandwiches is 0 things below happen
        try:
            num_sandwiches = int(input("How many sandwiches would you like to order? "))#num_sandwiches becomes an integer input   
            if num_sandwiches >= 1 and num_sandwiches <= 5:
                break#if input is between 1 and 5 if breaks
            else:
                print("Your order must be between 1 and 5")#if it isn't it asks the user to input a number between 1 and 5
        except ValueError:
            print("That is not a valid number, please enter a number between 1 and 5")#if something that isn't a number is inputted this happens

    print(num_sandwiches)#prints how much sandwiches they wanted to order

    #choose sandwich from menu
    for item in range(num_sandwiches):#it creates a loop, and the loop repeats for how much num_sandwiches is, which is how much pizzas is ordered
        while num_sandwiches > 0:#the loop ends when num_sandwiches becomes 0
            while True:
                try:
                    sandwich_ordered = int(input("Please choose your sandwiches by entering the number from the menu"))#sandwich_ordered allows an integer input
                    if sandwich_ordered >= 1 and sandwich_ordered <=10:
                        break#if sandwich is between 1 and 10 it proceeds
                    else:
                        print("Your sandwich order must be between 1 and 10  ")#if sandwich isnt between 1 and 10 it repeats
                except ValueError:
                    print("That is not a valid number, please enter a number between 1 and 10")#if sandwich isn't a integer it prints this 
            sandwich_ordered = sandwich_ordered - 1#this is so that it doesn't print the wrong things since we ahve the index numbers starting at 1 instead of 0
            order_list.append(sandwich_names[sandwich_ordered])
            order_cost.append(sandwich_prices[sandwich_ordered])#the inpuuted number is then sent to the sandwich names and prices which sends back the respective index number items.
            print("{} ${:.2f}" .format(sandwich_names[sandwich_ordered],sandwich_prices[sandwich_ordered]))#prints the sandwich names and prices together, prices have a dollar sign and are 2 d.p
            num_sandwiches = num_sandwiches-1#this is what helps create the loop by taking 1 away from num_sandwiches for every one that is ordered




#Print order out - including if order is delivery or pickup and names and price of each item - total cost




#Ability to cancel or proceed with order




#Create option for new order or to exit




#Main Funciton
def main(): #Created a function to run all the functions
    '''
    Purpose: To run all functions
    Parameters: none
    Returns: none
    '''
    welcome()
    order_type()
    menu()
    order_sandwich()


main() #Runs the main function 


