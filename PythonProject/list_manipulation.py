x = [2, "two", [1,2,3]]
length = len(x)
print(f' the list has the length of {length}')
print(f'index of 2 equals =',x[2])
print(f' the list has the length of ',len(x))

x1 = ["first", "second", "third", "fourth"]
print(x1)
print()
y = x1[:]
print(y)
y[0] = '1st'
print('the new y list =',y)  # can't concatenate list

print(x)
x[len(x):] = [3,18,21]   #appends to the end of the list
print(x)

x[:0] = [-1,0] # appends list to front of list
print(x)

x[1:-1] = [] # removes elements from the list from index 1 to last index
print(x)

print(x1,y)
x1.extend(y)
print(x1)

# insert function in lists
x1.insert(2, "frank")
print(x1)
value = "frank" in x1  # checks if the value exist in the list
print(value)

x1.remove('frank') # remove element frank from the list

print(x1)
x1.sort()
print(x1)
