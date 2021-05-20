# Q!. Take user input, create a Python list, find a value in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [6, 10, 45, 20, 35, 90, 80]

index = list1.index(20)
list1[index] = 200
print(list1)
