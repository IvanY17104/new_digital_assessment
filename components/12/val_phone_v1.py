question = ("Please enter your phone number ")  # test question

ph_low = 7
ph_high = 10

def check_phone(ph_low, ph_high, question):
    while True:
        try:  # this creates a loop
            num = int(input(question))
            # num asks for a integer input
            test_num = num
            count = 0
            while test_num > 0: 
                test_num = test_num//10
                # if num is larger than zero it will get divided by 10
                # so 1 digit gets removed
                count = count + 1
                # 1 will be added to count for every digit removed/counted
            if count >= ph_low and count <= ph_high:
                return num  #if count is between low and high it returns
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number")

phone = check_phone(ph_low, ph_high, question)
print(phone)
