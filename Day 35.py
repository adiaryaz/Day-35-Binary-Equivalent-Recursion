def binary_equivalent(number):
    if number == 0:
        return ""
    
    return binary_equivalent(number // 2) + str(number % 2)

number = int(input("Enter an integer: "))

if number == 0:
    print("The binary equivalent of 0 is 0.")
elif number > 0:
    print(f"The binary equivalent of {number} is {binary_equivalent(number)}.")
else:
    print(f"The binary equivalent of {number} is -{binary_equivalent(abs(number))}.")