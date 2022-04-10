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
num_sandwiches = int(input("How many sandwiches would you like to order? "))
print(num_sandwiches)


#choose sandwich from menu
print ("Please choose your pizzas by entering the number from the menu")
for item in range(num_sandwiches):
    while num_sandwiches > 0:
        sandwich_ordered = int(input())
        order_list.append(sandwich_names[sandwich_ordered])
        order_cost.append(sandwich_prices[sandwich_ordered])
        num_sandwiches = num_sandwiches-1

print(order_list)
print(order_cost)

#countdown until all sandwiches are ordered

#print order





