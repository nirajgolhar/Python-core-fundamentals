# print ('Lets start !')
data = ['three','banana','mango']
data2 =['papaya','palebhaaji']
# data2=['apple','banana']
# data.append('grapes')
# data.insert(1,'cherry')
# data.pop(3)
# data3=data2+data
# # print(data)
# print(data3)

#insert method
data.insert(0,'mango')
print(data)

#pop method
data.pop(3)
print(data)

#append method
data.insert(21,'mango')
data.append('banana')
print(data)

#extend method
data.extend(data2)
print(data)

#append method with parameter as list variable
data.append(data2)
print(data)

#length method for knowing length of list
listt = ['daya','praduman','fedrik','abhijeet']
print(len(listt))
print('done, we have prnted the length!')

#remove method
listt.remove('daya')
print(listt)

#if condition on list
fruits = ['grapes','apple','pineapple']
if 'banana' in fruits:
    fruits.remove('banana')
    print(fruits)
else:
    print ('not present')

#count method and sort method  TIP:sort methos needs to be performed seperate and then printed
fruits1 = ['grapes','apple','pineapple','guavax']
print(fruits1.count('grapes'))
fruits.sort()
print(fruits)

#sortred method
city=['palghar','mumbai','arnala','thane','pune','nashik']
print(sorted(city))


#clear method which clears the list and makes it empty
fruits.clear()
print(fruits)

#list -->sublist-->accesing it through index
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])


# print([4,5,7] is [4,5,7])  # o/p False but
# print([4,5,7] == [4,5,7]) # o/p True why?

#for loop
matrix1 = [[1,4,4],[22,22,34]]
for subList in matrix1:
    for i in subList:
        print(i)




