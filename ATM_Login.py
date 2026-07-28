pin= (int(input("enter your atm pin")))
if pin==1234:
    amount=(int(input("enter amount to withdraw")))
    if amount <= 5000:
        print ("your Transaction is succesfull")
    else:
        print ("Insufficient Balance")
else:
    print ("Your pin is incorrect")