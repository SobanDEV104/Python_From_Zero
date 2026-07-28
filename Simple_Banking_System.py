choice=int(input("1.Check balance\n2.Deposit\n3.Withdraw\n4.Exit.\n "))
balance= 10000
if choice ==1:
    print ("YOUR TOTAL BALANCE IS:",balance)
elif choice ==2:
    amount= int(input(("enter amount to deposit")))
    balance= balance + amount
    print ("your new balance is: ",balance)
elif choice==3:
    withdraw=int(input("enter amount to withdraw"))
    if withdraw <=balance:
        balance= balance - withdraw
        print("your remaining balance is: ", balance)
    else:
        print ("Insufficient Balance")
elif choice ==4:
    print ("YOU SUCCESFULLY EXIT OUR SYSTEM")
else:
    print("Invalid Choice")
