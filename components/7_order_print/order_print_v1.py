#names = ["Ivan", "James", "Matthew", "Ryan", "Felix", "Grace", "Amy", "Alice", "Lara",  "Rayyan"]#List of random names

#sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']
#list of sandwich names

#sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]
#list of sandwich prices

order_list = ['Ham','Chicken','Egg and Cheese']
order_cost = [4.50, 4.50, 5.50]#lists to store sandwich orders and costs

#customer_details = {}#a dictionary to store customer details

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
    count = count + 1




