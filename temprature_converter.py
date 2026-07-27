choice = int(input("Choose an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n"))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius:\n"))
    fahrenheit = (9 / 5) * celsius + 32
    print("Temperature in Fahrenheit =", fahrenheit)

if choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit:\n"))
    celsius = (5 / 9) * (fahrenheit - 32)
    print("Temperature in Celsius =", celsius)
else:
    print("invalid choice")
