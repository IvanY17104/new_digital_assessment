#Welcome message and Random name genrator component
#Creates a random name from a random name generator
#Prints a welcome message that includes the random name

import random
from random import randint #this import allows me to create a random number generator

names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

num = randint(0,9) #num will give a random number (randint) between 0 to 9

name = (names[num]) #each name in names has a number associated with it, and num  will give a random number, so 'name' will give a random name
print("Welcome to Ivan's Sandwich Store!")
print("My name is",name,"and I will help you take your Sandwich orders.") #This is the welcome message that will show up