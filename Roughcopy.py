# def sum_of_number(n):
#     return sum(n)

# x = [1,2,3,4,5]
# y =[10, -5, 7, 8, -2]
# print(sum_of_number(y))

# def largest(arr):
#     for i in arr:
#         for j in i+1:
#             if arr[i] < arr[j]:
#                 pass
#     return i

# x = [1,2,3,4,5]
# y = [6,7]
# print(largest(x))


# def count_even_odd(lst):
#     # Your code goes here
#     even = 0
#     odd = 0
#     for i in lst:
#         if i % 2 == 0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd

# print(count_even_odd(x))

# def is_subset(lst1, lst2):
#     # Your code goes here
#     x = set(lst1).issubset(set(lst2))
#     return x

# print(is_subset(x,y))
# x = [1, 7, 3, 10, 5]
# def defferent(lst) -> int:
#     largest = 0
#     scond = 0
#     for i in range(1, len(lst)):
#         if lst[i] > largest:
#             largest = lst[i]
#             scond = lst[i-1]
#     return largest - scond


# print(defferent(x))

# def l(lst):
#     max_diff = 0  # Start with 0 difference
#     for i in range(len(lst) - 1):
#         diff = abs(lst[i] - lst[i + 1])  # Absolute difference between consecutive elements
#         if diff > max_diff:
#             max_diff = diff
#     return max_diff
# print(l(x))



# def merge_two_sorted_lists(list1,list2):
#     # Your code goes here
#     # i = list1[0]
#     ans1 = 0
#     ans2 = 0
#     new = []
#     for i in range(1,len(list1)):
#         if i < list1[i]:
#             ans1 = list1[i]
#             new.append(ans1)
#     for j in range(1,len(list2)):
#         if j < list2[j]:
#             ans2 = list2[j]
#             new.append(ans2)

#     return new

# def merge_two_sorted_lists(list1, list2):
#     # Your code goes here
#     x = list1 + list2
#     return x.sort()    

 

# x = [1,2,3,7]
# y = 3
# print(merge_two_sorted_lists(x,y))

# def rotate_list(lst, k):
#     # Your code goes here
#     for i in range(1,len(k)):
#         lst.pop(i)
#     return lst

# print(rotate_list(x,y))

# def merge_lists_to_dictionary(keys, values):
#     # Your code goes here
#     return dict(zip(keys,values))

# keys = ['a', 'b', 'c'], 
# values = [1, 2, 3]
# # {'a': 1, 'b': 2, 'c': 3}

# print(merge_lists_to_dictionary(keys=keys,values=values))


# def merge_three_dictionaries(dict1, dict2, dict3):
#     # Your code goes here
#     return {**dict1,**dict2,**dict3}


# dict1= {'a': 1, 'b': 2}, 
# dict2 ={'c': 3, 'd': 4}, 
# dict3 = {'e': 5, 'f': 6}
# print(merge_three_dictionaries(dict1,dict2,dict3))


# def count_word_frequency(sentence):
#     # Your code goes here
#     result = {}
#     for i in sentence.split():
#         if i in result:
#             result[i]+=1
#         else:
#             result[i]=1
#     return result

# print(count_word_frequency("hello world hello"))

# def is_palindromic_tuple(tup):
#     # Your code goes here
#     if len(tup) == len(tup):
#         if tup == tup[::-1]:
#             return True
#         else:
#             return False
    
# x =(1, 2, 3, 2, 1)
# y =('a', 'b', 'c', 'b', 'a')
# z =('x', 'y', 'z', 'x')
# print(is_palindromic_tuple(z))


# is_number = 10
# n = 1
# while n < is_number:
#     print(n)
#     n+=1
# print(n)

# a = (1,2,3,4,5)
# y = list(a)
# x = y.append(6)
# print(tuple(x))

# Program to display the Fibonacci sequence up to n-th term

       

# def fibonacci(x):
#     n1, n2 = 0 ,1 
#     count = 0
#     if x <= 0 :
#         return "Enter positove integer !"
#     elif x == 1 :
#         return x
#     else:
#         while count < x:
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth 
#             count += 1



# print(fibonacci(7))


# import numpy as np 

# arr = np.array([1,2,3,4,5])
# print(arr)



# arrr = np.array([1,2,3,4,5])
# arr1 = arrr.reshape(5,1)
# arr1

# class Vehicle:
#     def start(self):
#         print("Vehicle starting...")

# class Car(Vehicle):
#     def start(self):
#         print("Car starting...")
#         super().start()

# # Test
# car = Car()
# car.start()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         self.__age = age

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

# # Test
# student = Student('John', 20, 'S123')
# print(student.get_name(), student.get_age(), student.student_id)
# student.set_name('Alice')
# student.set_age(22)
# print(student.get_name(), student.get_age(), student.student_id)



# def flatten_list(flatten):
#     lists = [item for sub_list in flatten for item in sub_list]
#     return lists

# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# flattened = flatten_list(nested_list)
# print("Original nested list:")
# print(nested_list)
# print("Flattened list:")
# print(flattened)


import numpy as np
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(a[1:3, 1:3])

array = np.random.randint(1, 21, size=(5, 5))
print("Original array:")
print(array)

print(array[0,:],array[-1,:],array[1:-1,0],array[1:-1,-1])
