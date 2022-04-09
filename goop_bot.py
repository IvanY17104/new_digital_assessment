#Goop Store program

import random
from random import randint #this import allows me to create a random number generator

names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

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
    print("Welcome to the Goop Store!")
    print("My name is",name,"and I will help you take your Goop orders.") #This is the welcome message that will show up




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
                    break#breaks loop

                elif delivery == 2:
                    print("Pickup")#if 2 is inputted it prints pickup
                    pickup()#will activate pickup function and begin asking things for pickup
                    break#breaks loop
            else:
                print("The number must be 1 or 2")#prints this when a number is less than 1 or greater than 2 

        except ValueError:
            print("That is not a valid number, please enter 1 or 2")#this prints when expected values arent inputted



#Pickup information - name and phone number
def pickup():
    question = ("Please enter your name ")#asks the user to enter their name
    customer_details['name'] =  not_blank(question)#customer_details goes off to not_blank, later not_blank is sent back to customer_details after input

    question = ("Please enter your phone number ")#asks the user to enter theirn phone number
    customer_details['phone'] = not_blank(question)#same as above

    print(customer_details['name'])
    print(customer_details['phone'])#prints the 2 inputs stored in dictionary



#Delivery Infornation - name address and phone




#Choose total number of items - max 5




#Goop Menu




#Goop Ordering - from menu - print each item with cost




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


main() #Runs the main function 


