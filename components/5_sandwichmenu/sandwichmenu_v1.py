sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']#list of sandwich names

sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]#list of sandwich prices

number_sandwich = 10

print("How many pizzas would you like to order?")#asks user
num_sandwich = int(input())#num_sandwich allows an input

for count in range (number_sandwich):
    print(count,sandwich_names[count], sandwich_prices[count])






