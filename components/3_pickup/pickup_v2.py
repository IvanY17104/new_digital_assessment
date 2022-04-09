print("Please enter the pickup information")#asks the user to enter their information

valid = False
while not valid:#this along with line above creates a loop
    name = input("Please enter your name ")#asks for user name and allows input
    if name != "":#if name isn't blank
        print (name)
        break#ends loop
    else:
        print("Sorry this cannot be blank")#this prints if name is blank

valid = False
while not valid:#loop
    phone = input("Please enter your phone number")#asks for user phone number and allows input
    if phone != "":#if phone isn't blank
        print(phone)
        break#ends loop
    else:
        print("Sorry this can't be blank")#this prints if phone is blank
 
print(name)
print(phone)#prints the name and phone number


