#5. Display the last digit and first digit of the given number.
num = int(input("Enter a number: "))
num1 = num % 10 
num2 = int(str(num)[::-1])
first_digit = num2 % 10
print("The last digit is ", num1)
print("The first digit is ", first_digit)