# Advance Data Structures
# List - List is collection of items or list of items
# Duplicates are allowed in List
# Syntex : always in squre brackets [] - multiple data types also allowed
# List will be stored with Index
from operator import truediv

my_list = [1, 10, 20]
My_list1 = ["jab", 10, 10.2, True]
print(my_list)
print(len(my_list))
print((my_list)[2])

for item in my_list:
    print(item, end= " ")
# Append() -  object to the end of the list
my_list.append(5)
print(my_list)

# Extend() - New list will be added

my_list.extend([10,20,30])
print(my_list)

# insert () - will insetr the value in index
my_list.insert(0, "Shaik")
print(my_list)

# remove() - We can remove the index wise
my_list.remove(1)
print(my_list)

# my_copy_list = my_list.copy - we can copy the list.
my_copy_list = my_list.copy()
print(my_copy_list)
my_copy_list.remove("Shaik")
# Sort - we can sort the int values
my_copy_list.sort()
print(my_copy_list)
# POP - pop will remove the last index value

my_copy_list.pop()
print(my_copy_list)
