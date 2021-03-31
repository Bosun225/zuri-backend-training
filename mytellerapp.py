def main():
    import datetime
    import time
    now = datetime.datetime.now()
    balance = [3000, 5000, 7000, 9000]
    name = input("Please enter your account name:")
    allowedUser = ['Abdul', 'Qudus', 'Bimpe', 'Ade']
    allowedPassword = ['PasswordAbdul', 'PasswordQudus', 'PasswordBimpe', 'PasswordAde']

    if(name in allowedUser):
        password = input("Please enter your password:")
        userId = allowedUser.index(name)

        if(password == allowedPassword[userId]):
            print("Hello %s you are welcome to the Teller Machine today:" %name, now.strftime("%y-%m-%d %H:%M"))
            time.sleep(3)
            print("Please select your preferred transaction below:")
            time.sleep(3)
            print('1. Withdrawal')
            time.sleep(1)
            print('2. Deposit')
            time.sleep(1)
            print('3. Balance')
            time.sleep(1)
            print('4. Complaint')
            time.sleep(1)
            print('5. Cancel Transaction')
            selection = int(input(">>>"))
            if(selection == 1):
                print('How much would you like to withdraw')
                amt = int(input(">>>"))
                balance = int(balance[userId]) - amt
                print("Take Your Cash")
            elif(selection == 2):
                print("How much would you like to deposit")
                amt = int(input(">>>"))
                balance = int(balance[userId]) + amt
                print("Your deposit was successful")
                print(f'Your current balance is: {balance}')
                time.sleep(5)
            elif(selection == 3):
                print(f'Your current balance is:', balance[userId])
                time.sleep(5)
            elif(selection == 4):
                print("What issue would you like to report")
                msg = (input("Please type your complaint here \n >>>"))
                time.sleep(2)
                repeat = (input("To perfrom another Transaction Type 'yes' to confirm or 'no' to end your Transaction\n >>>")).lower()
                if(repeat  == 'yes'):
                    main()                    
                else:
                    print('Thank you for contacting us')
                exit()                                                                                                
                                                 
            else:
                print('Thank you for visiting our Teller Machine today, Do enjoy the rest of your day. :o)')                   
        else:
            print("Password Incorrect, Please try again")

    else:
        print('Name not found, please try again')

main()
