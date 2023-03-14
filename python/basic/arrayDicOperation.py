# 创建字典
my_dict = {'name': 'John', 'age': 30}

# 获取字典中的值
name = my_dict['name']
age = my_dict.get('age')

# 修改字典中的值
my_dict['age'] = 40

# 添加键值对到字典中
my_dict['city'] = 'New York'

# 删除字典中的键值对
del my_dict['age']
my_dict.pop('city')

# 遍历字典
for key, value in my_dict.items():
    print(key, value)

# 创建列表
my_list = [1, 2, 3, 4, 5]

# 获取列表中的元素
first_element = my_list[0]
last_element = my_list[-1]

# 修改列表中的元素
my_list[0] = 6

# 在列表末尾添加元素
my_list.append(6)

# 在列表中插入元素
my_list.insert(2, 7)

# 删除列表中的元素
my_list.remove(7)
my_list.pop()
del my_list[0]

# 遍历列表
for item in my_list:
    print(item)
    
# 合并多个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
my_list = list1 + list2 + list3

# 列表切片
my_list_slice = my_list[2:6]  # 返回第3个元素到第6个元素

# 列表推导式
my_list_squared = [x**2 for x in my_list]

# 使用filter()和lambda表达式过滤列表
my_list_filtered = list(filter(lambda x: x % 2 == 0, my_list))