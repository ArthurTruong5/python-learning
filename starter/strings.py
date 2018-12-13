name = 'Arthur'
age = 37

# console.log
print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('{1}, {2}, {3}'.format('a','b','c'))

# string methods

s = 'hello there world'

# capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# make all lower
print(s.lower())

# swap case
print(s.swapcase())

# get length
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# count
sub = "h"
print(s.count(sub))
