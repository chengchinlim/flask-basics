# Comparisons: ==, !=, ... Same as Java

list1 = ['apple', 'orange']
list2 = ['apple', 'orange']

print(list1 == list2) # (Deep Equals) Opposite of Java 
print (list1 is list2)

number = 2
if number == 1:
    print('Number is one')
elif number == 2:
    print('Number is two')
else:
    print('Number is other number')

# 'in' is contains() in Java
if 'apple' in list1:
    print('Apple exists')
else:
    print('Not exist in list')

