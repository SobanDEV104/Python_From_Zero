age = float(input("Enter your age: "))
cnic = str(input("Do you have cnic? yes or no"))
if age >= 18 and cnic == "yes":
    print ("you are eligible to vote")
else:
    print("you are not eligible")