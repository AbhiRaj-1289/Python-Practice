#Python function to calculate tip
#Author : Abhinav Raj

def tip():
    print("Welcome to Tip Calcuulator")
    bill = float(input("Enter the bill amount Rs: "))
    service = input("How was the service? \n 1. Terrible \n 2. Bad \n 3. Good \n 4. Great \n")
    if service == "1":
        tip = bill * 0.05
        print("Tip amount is Rs: ", tip)
    elif service == "2":
        tip = bill * 0.10
        print("Tip amount is Rs: ", tip)
    elif service == "3":
        tip = bill * 0.15
        print("Tip amount is Rs: ", tip)
    elif service  == "4":
        tip = bill * 0.20
        print("Tip amount is Rs: ", tip)
    else:
        print("Invalid Input")
    print("Thnakyou! for visiting. ")
    print("Do visit again.")

tip()