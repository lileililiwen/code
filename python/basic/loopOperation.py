# for循环遍历列表
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# for循环遍历字典中的键
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# for循环遍历字典中的值
for value in my_dict.values():
    print(value)

# for循环遍历字典中的键值对
for key, value in my_dict.items():
    print(key, value)

# while循环遍历列表
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# 使用enumerate()函数同时遍历列表的下标和元素
for index, value in enumerate(my_list):
    print(index, value)

# 使用zip()函数同时遍历多个列表
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(item1, item2)

# 使用reversed()函数倒序遍历列表
for item in reversed(my_list):
    print(item)

# 使用sorted()函数按照指定方式排序后遍历列表
my_list = [5, 2, 1, 3, 4]
for item in sorted(my_list):
    print(item)
for item in sorted(my_list, reverse=True):
    print(item)