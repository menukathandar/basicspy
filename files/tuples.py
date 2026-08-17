# A tuple is an (immutable) ordered list of values. 
# A tuple is in many ways similar to a list; 
# one of the most important differences is that tuples can be used 
# as keys in dictionaries and as elements of sets, while lists cannot. 
d = {(x, x+1): x for x in range(5)} #Create a dictionary with tuple
t = (4, 5)
print(d)
print(type(t)) # prints <class 'tuple'>
print(d[t]) # Prints 4
print(d[(1,2)]) # prints 1
# Note: The tuple qualifies to be a key in dictionary because 
#dictionary keys in python must be hashable(immutable basically)
#and tuples qualify as it can't be changed after creation
# (Unlike lists which can't be used as keys)