list = ['Cheng', 'Glenn', 'Kim'] # same as array (mutable) in JS
tuple = ('Cheng', 'Lim', 'pizza') # immutable
set = {'Cheng', 'Chin', 'Lim'} # same as Set in Java
set2 = {'Cheng', 'Lim'}

print(list[0])
list.append('Jack')
print(list)

print(tuple[1])

set.add('pizza')
set.add('pizza')
print(set)

diff = set.difference(set2) # Get the difference between two sets
print(diff)
union = set.union(set2) # Get the combination of two sets
print(union)
intersect = set.intersection(set2)
print(intersect)

numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers] # map in JS (New list is created)

fruits = ['apple', 'orange', 'pear']
filteredFruits = [fruit for fruit in fruits if fruit.startswith('a')]
print(filteredFruits)

nameToAge = {'Cheng': 23, 'Kim': 24, 'Yao': 25}
print(nameToAge['Cheng'])

for name, age in nameToAge.items(): # Kotlin Map Entries
    print(f'{name}: {age}')

if ('Cheng' in nameToAge):
    print('Cheng inside dictionary')

head, *tail = [1, 2, 3, 4, 5] # split the list
print(tail)

users = [
    ('Cheng', 'pizza'),
    ('Yao', 'burger')
]

users_map = {user[0]: user for user in users}
print(users_map['Yao'])
