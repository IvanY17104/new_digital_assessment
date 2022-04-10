sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']#list of sandwich names

sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]#list of sandwich prices

order_list = []
order_cost = []#lists to store sandwich orders and costs

def menu():
    number_sandwich = 10

    for count in range (number_sandwich):
        print("{} {} ${:.2f}" .format(count+1,sandwich_names[count], sandwich_prices[count]))
        #the 3 {} brackets contain count sandwich name and price count, so things that we do in those affect the count print
        #dollar sign and :.2f makes the sandwich prices have a dollar sign infront, and have 2 decimal places
        #count +1 makes it so that the index numbers start at 1 and not 0
menu()

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
print ("Please choose your pizzas by entering the number from the menu")#asks the users to choose what they want to order
for item in range(num_sandwiches):#it creates a loop, and the loop repeats for how much num_sandwiches is, which is how much pizzas is ordered
    while num_sandwiches > 0:#the loop ends when num_sandwiches becomes 0
        sandwich_ordered = int(input())#sandwich_ordered allows an integer input
        order_list.append(sandwich_names[sandwich_ordered])
        order_cost.append(sandwich_prices[sandwich_ordered])#the inpuuted number is then sent to the sandwich names and prices which sends back the respective index number items.
        num_sandwiches = num_sandwiches-1#this is what helps create the loop by taking 1 away from num_sandwiches for every one that is ordered

print(order_list)
print(order_cost)#prints the ordered items with their costs

#countdown until all sandwiches are ordered

#print order





