# Dictionaries in python stores (key, value) pairs 
dictionary = {'Sun' : 'Sunny', 'mon' : 'Windy', 'Tue' : 'Cloudy'}
print(dictionary['Sun']) # Prints sunny
print('Sunny' in dictionary) # Prints false because "in" checks for key in the dictionary not the value
print('sun' in dictionary) #FAlse (Case sensitive)
print('Sun' in dictionary) # True
dictionary['Wed'] = 'Rainy'
print(dictionary)

print(dictionary.get('Sun', 'N/A')) # Prints Sunny
print(dictionary.get('Thurs', 'N/A')) # Prints N/A
del dictionary['Wed'] # removes elements
print(dictionary)


#Loops in dictionaries
for dict in dictionary:
    weather = dictionary[dict]
    print(f'The weather on {dict} is {weather}.')


#Comprehensions in dictionaries
nums = [0,1,2,3,4,5]
even_num_to_square = {x: x **2 for x in nums if x % 2 == 0}
print(even_num_to_square) # prints {0: 0, 2: 4, 4: 16}