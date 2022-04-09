sandwich_names = ['Egg','Ham','Chicken','Egg and Cheese','Ham and Cheese','Chicken and Cheese','Vegan Special','Meat Special','Ivan Special','Special Deluxe']
#list of sandwich names

sandwich_prices = [4.50, 4.50, 4.50, 5.50, 5.50, 5.50, 6.50, 6.50, 7.50, 11.50]
#list of sandwich prices

number_sandwich = 10

for count in range (number_sandwich):
    print("{} {} ${:.2f}" .format(count+1,sandwich_names[count], sandwich_prices[count]))
    #the 3 {} brackets contain count sandwich name and price count, so things that we do in those affect the count print
    #dollar sign and :.2f makes the sandwich prices have a dollar sign infront, and have 2 decimal places
    #count +1 makes it so that the index numbers start at 1 and not 0