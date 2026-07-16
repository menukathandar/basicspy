#6. Accept numbers from the user until 0 is input. Find the sum of the numbers. Use
#a while loop.
num1 = int(input("Enter a number to find sum until 0: "))
total_sum = 0
while(num1 != 0):
    num2 = int(input(("Enter another number: ")))
    #print(num2)
    added_sum = total_sum+num2
    added_sum2 = added_sum + num1
    total_sum = added_sum 
    #print(added_sum2)
    if num2 == 0:
        print("The total sum of the numbers you added is: ", added_sum2)
        break
else:
    print("The loop ended")