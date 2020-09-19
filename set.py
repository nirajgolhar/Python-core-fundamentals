# s = {1,2,3,2}
# print(s)

# s = {1,1.0,3,4}
# print(s)

# s = {1,1.1,'string'}
# print(s)
# print(type(s))

# s = {1,1.1,'string',[1],{1:1}}
# print(s)

# l = [1,2,3,4,5,5,5,5,6,7,7,8]
# s = set(l)
# print(s)

# s = {1,2,3}
# s.add(4)
# print(s)

# s = {1,2,3}
# s.add(4)
# s.add(4)
# print(s)

# s = {1,2,3}
# s.remove(1)
# print(s)

# s = {1,2,3,4,4}
# s.discard(4)
# print(s)

# s = {1,2,3,4,4}
# s.clear()
# # print(s.clear())
# print(s)

# s = {1,2,3,4}
# s1 = s.copy()
# print(s)
# print(s1)

# s = {'a','b','c'}
# if 'a' in s:
# print('present')
# else:
# print('not present')

# s = {'a','b','c'}
# for item in s:
# print(item)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# union_set = s1 | s2
# print(union_set)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# union_set = s1 & s2
# print(union_set)

# user = {'name' : 'Kundan', 'age' : 22}
# print(user)
# print(type(user))

# user = dict(name = 'Kundan', age = 22)
# print(user)
# print(user[0])

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# print(user_info['fav_movies'])

# user_info = {}
# user_info['name'] = 'Kundan'
# user_info['age'] = 18

# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }

# if 'names' in user_info:
# print('present')
# else:
# print('not present')

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# if 'Kundan' in user_info.values():
# print('present')
# else:
# print('not present')

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# for i in user_info:
# print(i)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# for i in user_info.values():
# print(i)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }

# user_info['fav_songs'] = ['song1','song2']
# user_info['location'] = ['bangalore']
# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# popped_item = user_info.pop('fav_tunes')
# print("popped item is {}".format(popped_item))
# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }
# popped_item = user_info.popitem()
# print(user_info)
# print(type(popped_item))

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }

# more_info = {'state':'bangalore','Address':'Marathalli'}
# user_info.update(more_info)
# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# }
# user_info.update({'ram':'sita'})
# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }

# more_info = {'name' : 'Kundan Kumar','state':'bangalore','Address':'Marathalli'}
# user_info.update(more_info)
# print(user_info)

# user_info = {
# 'name' : 'Kundan',
# 'age' : 22,
# 'fav_movies': ['coco','kimi no na wa'],
# 'fav_tunes' : ['awakening','fairy tale']
# }

# more_info = {'name' : 'Kundan Kumar','state':'bangalore','Address':'Marathalli'}
# user_info.update({})
# print(user_info)

# d = {'name': 'unknown', 'age': 'unknown'}
# print(d)

# d = dict.fromkeys(['name','age','height'],'unknown')
# print(d)

# d = dict.fromkeys('abc','unknown')
# print(d)

# d = dict.fromkeys(range(1,5),'unknown')
# print(d)

# d = dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)

# d = dict.fromkeys(['name','age'],'unknown')
# print(d['name'])

# d = {'name':'kundan','age':22}
# print(d.get())

# d = dict.fromkeys(['name','age'],'unknown')
# print(d.get('name'))

# d = dict.fromkeys(['name','age'],'unknown')
# print(d.get('hello'))

# d = {'name' : 'Kundan', 'age' : 22}
# if 'name' in d:
# print('present')
# else:
# print('not present')

# d = {'name' : 'Kundan', 'age' : 22}
# if d.get('name'):
# print('present')
# else:
# print('not present')

# d = {'name' : 'Kundan', 'age' : 22}
# print(d.popitem())
# print(d)


# def cube_finder(n):
# cubes = {}
# for i in range(1,n+1):
# cubes[i] = i**3
# return cubes

# print(cube_finder(10))

# def word_counter(s):
# count = {}
# for char in s:
# count[char] = s.count(char)
# return count
#
# print(word_counter('kundan'))


# s = {1,2,3,2}
# print(s)

# s = {1,1.0,3,4}
# print(s)

# s = {1,1.1,'string'}
# print(s)
# print(type(s))

# s = {1,1.1,'string',[1],{1:1}}
# print(s)

# l = [1,2,3,4,5,5,5,5,6,7,7,8]
# s = set(l)
# print(s)

# s = {1,2,3}
# s.add(4)
# print(s)

# s = {1,2,3}
# s.add(4)
# s.add(4)
# print(s)

# s = {1,2,3}
# s.remove(1)
# print(s)

# s = {1,2,3,4,4}
# s.discard(4)
# print(s)

# s = {1,2,3,4,4}
# s.clear()
# # print(s.clear())
# print(s)

# s = {1,2,3,4}
# s1 = s.copy()
# print(s)
# print(s1)

# s = {'a','b','c'}
# if 'a' in s:
# print('present')
# else:
# print('not present')

# s = {'a','b','c'}
# for item in s:
# print(item)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# union_set = s1 | s2
# print(union_set)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# union_set = s1 & s2
# print(union_set)

