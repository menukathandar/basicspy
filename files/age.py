#2. Take the age of a person from the user and display whether the person is a child
#(age .< 12) or teenager (age .< 18) or adult (age .< 50) or a senior citizen (age
#. >= 50).
# age = int(input("Enter your age:  "))
# while(age>0):
#     if(age < 12):
#         print("You are a child.")
#         break
#     if(age < 18):
#         print("You're a teenager. ")
#         break
#     if(age < 50):
#         print("You're an adult")
#         break
#     else:
#         print("You are a senior citizen.")
#         break
# else:
#     print("Please enter a valid age.")

age = int(input("Enter your age:  "))
if(age > 0):
    if(age < 12):
        print("You are a child.")
    elif(age < 18):
        print("You're a teenager. ")
    elif(age < 50):
        print("You're an adult")
    elif(age >= 50):
        print("You are a senior citizen.")
else:
    print("Please enter a valid age.")