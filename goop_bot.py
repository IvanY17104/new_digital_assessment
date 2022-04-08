#Goop Store program

import random
from random import randint #this import allows me to create a random number generator

names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

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




#Pickup information - name and phone number




#Delivery Infornation - name address and phone




#Choose total number of items - max 5




#Goop Menu




#Goop Ordering - from menu - print each item with cost




#Print order out - including if order is delivery or pickup and names and price of each item - total cost




#Ability to cancel or proceed with order




#Create option for new order or to exit




#Main Funciton
def main(): #Created a function to run welcome
    '''
    Purpose: To run all functions
    Parameters: none
    Returns: none
    '''
    welcome()

main() #Runs the main function 


