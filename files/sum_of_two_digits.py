num  = int(input("Enter a number to display the sum of it's digits : ")) 
sum = 0
while(num > 0):
    num1 = num % 10
    remaining_num = num // 10
    sum = sum + num1
    num = remaining_num
print("sum of digits is ", sum)