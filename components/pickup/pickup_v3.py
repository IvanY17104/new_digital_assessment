customer_detail = {}#a dictionary to store

print("Please enter the pickup information")#asks the user to enter their information

valid = False
while not valid:#this along with line above creates a loop
    customer_detail['name'] = input("Please enter your name ")#asks for user name and allows input
    if customer_detail['name'] != "":#if name isn't blank
        print (customer_detail['name'])
        break#ends loop
    else:
        print("Sorry this cannot be blank")#this prints if name is blank

valid = False
while not valid:#loop
    customer_detail['phone'] = input("Please enter your phone number")#asks for user phone number and allows input
    if customer_detail['phone'] != "":#if phone isn't blank
        print(customer_detail['phone'])
        break#ends loop
    else:
        print("Sorry this can't be blank")#this prints if phone is blank
 
print(customer_detail['name'])
print(customer_detail['phone'])#prints the name and phone number