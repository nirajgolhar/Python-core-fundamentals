# List Comprehension:


# Que: i want a (letter ,num)pair for each letter in 'abcd' and each number for '0123'
# sol 1 with nested for loops
# my_list=[]
# for letter in 'abcd':
#     for number in range(4):
#         my_list.append((letter,number))
# print(my_list)

# sol 2 with list Comprehension:
# my_list = []
# my_list = list((number, letter) for number in 'abcd' for letter in range(4))
# print(my_list)

# Dictonaries Function:




# ln=["shubham patil","niraj golhar","arun dube","joseph joy","swapnil poojari"]
# l=ln.sort(key=lambda name: name.split(" ")[-1].lower())
# print (l)


"""list comprehension
for simplyfying the process of creating empty list and adding single items at time using for loop
values=[(Expression) for (value) in (collection) ]
values=[(Expression) for (value) in (collection) if (conditon)]
"""

# reminder5=[i**2 %5 for i in range(1,101)]
# print(reminder5)

# movies=["Gattaca","ghost rider","race","Ready","gandhi","lion king"]
# f=[]
# for i in movies:
#     f.append(i.title())
# print(f)
# g_movies=[title for title in f if title.startswith("G") ]
# print(g_movies)

#cartesian product
# A=[1,3,5,7,9]
# B=[2,4,6,8]
# C=[5,7,9,7]
# car_pro=[(c,a,b) for c in C for a in A for b in B ]
# print(car_pro)


# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# squares = [i**2 for i in range(1,11) if i%2==0]
# print(squares)

# negative = []
# for i in range(1,11):
#     negative.append(-i**2)
# print(negative)

# negative = [-i**2 for i in range(1,11)])
# print(negative)

# print([-i for i in range(1,11)])

# names = ['Ram','Shyam','Gita','yomi']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# names = ['Ram','Shyam','Gita']
# print([name[0] for name in names])

# def reverse_str(l):
#     new_list = []
#     for name in l:
#         new_list.append(name[::-1])
#     return new_list
# print(reverse_str(['abc','tuv','xyz']))

# def reverse_string(l):
#     return [name[::-1] for name in l]
# print(reverse_string(['fhabc','tuv','xyz']))

# numbers = list(range(1,11))
# nums = []
# for i in numbers:
#     if i%2 == 0:
#         nums.append(i)
# print(nums)

# numbers = list(range(1,11))
# even_nums = [i for i in numbers if i%2 == 0]
# print(even_nums)

# numbers = list(range(1,11))
# print([i for i in numbers if i%2 == 0])

# print([i for i in range(1,11) if i%2 == 0])

# print([i for i in range(1,11) if i%2 != 0])

# def num_to_string(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]
#     # print (type(i))
# print(num_to_string([True,False,[1,2,3],1,1.0,3]))

# nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for i in nums:
#     if i%2 == 0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [i*2  if (i%2 == 0) else (-i) for i in nums ]
# print(new_list)

# new_list = []
# for j in range(3):
#     new_list.append([[1,2,3]])
# print(new_list)

# nested_comp = [[i for i in range(1,4)] for j in range(3)]
# print(nested_comp)

# square = {num:num**2 for num in range(1,11)}
# print(square)

# square = {"Square of {} is".format(num):num**2 for num in range(1,11)}
# # print(square)
# for k,v in square.items():
# print("{} :{}".format(k,v))

# string = 'kundan'
# word_count = {char:string.count(char) for char in string}
# print(word_count)

# d = {1:'odd', 2:'even'}
# odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(odd_even)



# s = [k**2 for k in range(1,11)]
# print(s)


# names = ['Ram','Mohit','Rohit']
# first = {name[0] for name in names}
# print(first)