def arm():
    num = int(input("Enter a Number : "))
    sum = 0
    if num in range(100,999):
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if num == sum:
            print(num, "is an Armstrong Number")
        else:
            print(num, "is not an Armstrong Number")
    else:
        print("Enter a number betwwen 100 to 999")
arm()