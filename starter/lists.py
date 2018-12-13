# A list is a collection which is ordered and changeable. Allows duplicate members

# create list
numbers = [1,2,3,4,5]

# using a constructor
numbers = list((1,2,3,4,5))
print(numbers)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# get value
print(fruits[1])

# get len - how many
print(len(fruits))

# append to list. similar to .push
fruits.append('Mangos')

# remove from list
fruits.remove('Grapes')

# insert into position
fruits.insert(2, 'Strawberries')

# remove from position
fruits.pop(3)

# reverse list
fruits.reverse()

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)
