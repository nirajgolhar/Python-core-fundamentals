# numbers = [1,2,3,4,1]
# print(numbers.index(4))

# numbers = [1,2,3,4,1,6]
# print(numbers.index(1,3))

# numbers = [1,2,3,4,5,6]
# def negative_list(numbers):
# negative = []
# for i in numbers:
# negative.append(i)
# return negative

# print(negative_list(numbers))


# def square_list(l):
# square = []
# for i in l:
# square.append(i**2)
# return square

# numbers = list(range(1,11))
# print(square_list(numbers))

# def reverse_list(l):
# l.reverse()
# return l

# words = ['hi','hello','helllooo']
# print(reverse_list(words))

# def reverse_list(l):
# return l[::1]

# words = ['hi','hello','helllooo']
# print(reverse_list(words))

# def reverse_list(l):
# r_list = []
# for i in range(len(l)):
# popped_item = l.pop()
# r_list.append(popped_item)
# return r_list

# numbers = [1,2,3,4]
# print(reverse_list(numbers))

# def reverse_elements(l):
# elements = []
# for i in l:
# elements.append(i[::-1])
# return elements

# words = ['abc','tuv','xyz']
# print(reverse_elements(words))

# def filter_odd_even(l):
# odd_nums = []
# even_nums = []
# for i in l:
# if i % 2 == 0:
# even_nums.append(i)
# else:
# odd_nums.append(i)
# output = [odd_nums,even_nums]
# return output

# nums = [1,2,3,4,5,6,7]
# print(filter_odd_even(nums))

# def common_finder(l1,l2):
# output = []
# for i in l1:
# if i in l2:
# output.append(i)
# return output
# l1 = [1,2,5,8]
# l2 = [1,2,7,6]
# print(common_finder(l1,l2))

# numbers = [6,60,2]
# print(min(numbers))

# numbers = [6,60,2]
# print(max(numbers))


# def greatest_diff(l):
# return max(l) - min(l)
# numbers = [6,60,2]
# print(greatest_diff(numbers))

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+=1
    return count

mixed = [1,2,3,[1,2],[3,4]]
print(sublist_counter(mixed))

