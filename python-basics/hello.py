name = 'Cheng'
lastName = 'Lim'
msg = f'Hello World, {name}'
msgTemplate = 'Hello World, {} {}'
msg2 = msgTemplate.format(name, lastName)
print(msg)
print(msg2)

ans = input('What is your favorite number? ') # same as Scanner in Java
print(ans) # as a string
favoriteNumber = int(ans) # parseInt() in JS
print(f'Favorite number in two decimal places is {favoriteNumber:.2f}')