#names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

#sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']
#list of sandwich names

#sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]
#list of sandwich prices

order_list = ['Ham','Chicken','Egg and Cheese']
order_cost = [4.50, 4.50, 5.50]#test list #lists to store sandwich orders and costs

customer_details = {'name':'Ivan','phone':'12317641','house':'12','street':'sandwich','suburb':'howick'}#test list #a dictionary to store customer details

#print("\n",customer_details['name'], "\n",customer_details['phone'], "\n",customer_details['house'], "\n",customer_details['street'], "\n",customer_details['suburb'])
#\n creates a gap infront of the printout

#print("\n Name:{} \n Phone:{} \n House Number:{} \n Street Name:{} \n Suburb:{}" .format(customer_details['name'] ,customer_details['phone'], customer_details['house'], customer_details['street'], customer_details['suburb'])) 

def print_order():
    total_cost = sum(order_cost)#total_cost is the sum of all prices in order_cost
    print("Customer Details")
    print(f"Name: {customer_details['name']} \nPhone: {customer_details['phone']} \nHouse Number: {customer_details['house']} \nStreet Name: {customer_details['street']} \nSuburb: {customer_details['suburb']}")
    #\n makes it go down one line, so they are all on seperate lines
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
        #this prints the order list with an 'Ordered' infront of it, and order cost with 'Cost' and $ infront of it with it also being 2 d.p
        count = count + 1#the count+1 is so that after it prints one order_cost it adds one and prints the next ones
    print()
    print(f"The total cost of the order is:${total_cost:.2f}")
    #this prints out the total cost of the order properly, with a $ sign and 2 d.p

print_order() 




