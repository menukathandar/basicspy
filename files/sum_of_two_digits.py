num  = 4511 
sum = 0
while(num > 0):
    num1 = num % 10
    remaining_num = num // 10
    sum = sum + num1
    num = remaining_num
print("sum of digits is ", sum)