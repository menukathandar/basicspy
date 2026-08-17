# Loops in python
# This is for loop
cities = ['Melbourne' , 'Sydney' , 'Brisbane']
for city in cities:
    print(city) # prints name of cities in each line


# If you want access to the index of each element within the body of a loop, 
# use the built-in enumerate function:
for idx, city in enumerate(cities):
    print(idx+1 , city) # Prints 1 Melbourne 2 Sydney 3 Brisbane in different lines