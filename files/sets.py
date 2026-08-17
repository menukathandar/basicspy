#Sets in python
# A set is an unordered collection of distinct elements
animals = {'cat' , 'dog' , 'monkey'}
print('cat' in animals)
animals.add('lion')
print(animals)

# Since sets are unordered so we cannot make assumptions 
# about the order in which we visit the elements of the set
for idx, animal in enumerate(animals):
    print(idx+1,animal)
animals.remove('lion')
print(f'The length of the elements in the given set is {len(animals)}.')
print(animals)