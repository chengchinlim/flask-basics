def hello(): 
    # variables are in local scope (Same as Java), 
    # but it can access outside scope variables
    print('Hello')

hello()

def add(x, y=0): # default param
    return x + y

print(add(5, 7))

myList = [1, 2, 3]
doubled = list(map(lambda x: x * 2, myList))