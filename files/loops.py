# Loops in python
# This is for loop
cities = ['Melbourne' , 'Sydney' , 'Brisbane']
for city in cities:
    print(city) # prints name of cities in each line


# If you want access to the index of each element within the body of a loop, 
# use the built-in enumerate function:
for idx, city in enumerate(cities):
    print(idx+1 , city) # Prints 1 Melbourne 2 Sydney 3 Brisbane in different lines


#List comprehensions: When programming, frequently we want to transform one type of data into another. 
# As a simple example, consider the following code that computes square numbers:
nums = [1,2,3,4,5]
squares = []
for i in nums:
    squares.append(i ** 2)
print(squares)

# Displaying only even squares
even_squares = []
for j in nums:
    if j % 2 == 0:
        even_squares.append( j ** 2)
print(even_squares) 

# We can make the above codes simpler using list comprehension
numbers = [20,30,40,50]
squares = [x ** 2 for x in numbers]
print(squares)

odd_squares = [x ** 2 for x in numbers if x % 2 == 1]
print(odd_squares)