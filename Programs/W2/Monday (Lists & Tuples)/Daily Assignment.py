# Write a program to reverse a list without using reverse().
list = [1, 2, 3, 4, 5]
reversed_list = []
for i in list:
    reversed_list.insert(0, i)
print(reversed_list)