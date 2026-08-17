#A list is the Python equivalent of an array, 
# but is resizable and can contain elements of different types: 
# Note: python starts index from “0”, for example, xs = [3,1,2], this first element of xs is xs[0] that is number 3.
my_list = [10,20,30]
print(my_list) #prints [10, 20, 30]
print(my_list[1]) # Prints 20 
print(my_list[-3]) # Prints 10
my_list.append('new1')
print(my_list)
my_list.pop()
print(my_list)


#Slicing in python
numbers = list(range(5))
print(numbers)
print(numbers[2:4]) # Prints 2,3
print(numbers[2:]) # prints 2,3,4
print(numbers[:2]) #prints 0,1
print(numbers[:]) # Gets a slice of whole lists and prints all elements
print(numbers[:-1]) #prints 0,1,2,3
numbers[2:4] = [25,35] # Assign new numbers 
print(numbers) # Prints [0, 1, 25, 35, 4]


# Length and sum of values in a list
print(len(numbers))
print(sum(numbers)) # It works if it only has numbers