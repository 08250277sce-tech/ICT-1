my_tuple = ("hello", 123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[-1]) # 1 or -1 will work
a, b = my_tuple #upacking
print(b)
new_tup = tuple (a)
print(new_tup)
concatenated_tuple = my_tuple + new_tup
print(concatenated_tuple)
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1])
del my_tuple
print(my_tuple) # this will raise error
