name = input("Enter your name: ")
for i in name:
    print(i)

# lterating over list
li = ["Python Programming", "Python Fundamental", "Python Interview Question"]
for x in li:
    print(x)

#range for list
lenli = len(li)
for x in range(lenli):
    print(li[x])

#tuple
new_tuple = tuple(li)
for x in new_tuple:
    print(x)

#range for tuple
lennew_tuple = len(new_tuple)
for x in range(lennew_tuple):
    print(new_tuple[0])

#set
new_set = set(li)
for x in new_set:
    print(x)

#Iterating over set and tuples
tup = ("John Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)

set1 = {10, 30, 20}
for x in set1:
    print(x)


    

