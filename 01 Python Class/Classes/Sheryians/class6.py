"""
    Data Structures
"""

# 1 List
# a = [12, 10, 40, 65, 80]
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[-1])

# for i in range(len(a)):
#     print(i)
#     print(a[i])

# b = ["banana", "apple", "orange", "grapes"]
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[-1])


# Methods
# numbers = [12, 40, 65, 80, 10]
# numbers.append(100)
# numbers.insert(1, 50)
# numbers.extend([1, 2, 3])
# numbers.remove(40)
# numbers.sort()
# numbers_copy = numbers.copy()
# numbers.clear()
# print(numbers)
# print(numbers_copy)


# Quiz for lists
# Q1. Print positive and negative elements of an List?
# l = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, 0]
# pos = []
# neg = []
# for i in range(len(l)):
#     if(l[i] >= 0):
#         pos.append(l[i])
#     else:
#         neg.append(l[i])
# print(pos)
# print(neg)

# Q2. Mean of List elements
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for i in range(len(num)):
#     sum += num[i]
# print(sum/len(num))

# Q3. Find the greatest element and print its index too
# num = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
# max = num[0]
# index = 0
# for i in range(len(num)):
#     if(num[i] > max):
#         max = num[i]
#         index = i
# print(f"greatest element is: {max}")
# print(f"index of greatest element is: {index}")

# Q4. Find the second greatest element
# num = [15, 25, 35, 45, 55, 25, 16, 105]
# max1 = num[0]
# max2 = num[1]
# for i in range(len(num)):
#     if(num[i] > max1):
#         max2 = max1
#         max1 = num[i]
#     elif(num[i] > max2):
#         max2 = num[i]
# print("second greatest element is: ", max2)

# Q5. Check if List is sorted or not
# num = [15, 25, 35, 45, 55, 25, 16, 105]
# # num = [1, 2, 3, 4, 5]
# flag = True
# for i in range(len(num)-1):
#     if(num[i] > num[i+1]):
#         flag = False
#         break
# if(flag):
#     print("List is sorted")
# else:
#     print("List is not sorted")



#  2. Tuples
# a = (12, 10, 40, 65, 5.5, "hemant")
# print(type(a))
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[-1])

# Tuple Traversing and methods
# a = (12, 10, 40, 65, 10)
# print(a.index(40))
# print(a.count(10))
# print(a.count(12))

# a, b, c, d = (12, 10, 40, 65)
# print(a)
# print(b)
# print(c)
# print(d)

# 3 Sets
# a = {10, 40, 65, 15, 10, }
# print(type(a))
# print(a)

# Set methods
# a = {1, 2, 3, 4}
# print(a)
# a.add(5)
# print(a)
# a.remove(2)
# print(a)
# a.discard(10)
# print(a)
# a.clear()
# print(a)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))


# 4 Dictionary
# d = {"name": "Hemant", "age": 20, "city": "Nashik"}
# print(type(d))
# print(d)
# print(d["name"])
# print(d["age"])
# print(d["city"])

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# print(type(d))
# print(d)
# d[2] = 100
# print(d)
# d.update({6: 60})
# print(d)
# del d[1]
# print(d)


# traverse
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# for i in d:
#     print(i, ":", d[i])

# Methods
# a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# b = a.copy()
# b[1] = 100
# print(a)
# print(b)

# b = a.get(2)
# print(b)

# print(a.items())



# Dictionary Questions
# Q1. Write a Python script to merge two Python dictionaries
# a = {1: 10, 2: 20, 3: 30}
# b = {3: 30, 5: 50, 6: 60}

# for i in b:
#     a[i] = b[i]
    
# print(a)

# Q2. Write a Python program to sum all the values in a dictionary?
# a = {1: 10, 2: 20, 3: 30}
# sum = 0
# for i in a:
#     sum += a[i]
# print(sum)


# Q3. Count the frequency of each element in list
# num = [1, 1, 5, 4, 5, 8, 7, 8, 8, 10, 10, 10, 10]
# dict = {}

# for i in num:
#     if(i in dict):
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)


# Q4.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 500, "d": 400}
d3 = {}
for i in d1:
    if(i in d2):
        d3[i] = d1[i] + d2[i]
    else:
        d3[i] = d1[i]
for i in d2:
    if(i not in d1):
        d3[i] = d2[i]
print(d3)







