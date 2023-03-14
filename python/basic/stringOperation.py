# 字符串拼接
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"

# 字符串格式化
name = "Alice"
age = 25
result = "My name is {} and I am {} years old".format(name, age)
print(result)  # Output: "My name is Alice and I am 25 years old"

# 字符串切片
text = "Hello World"
result = text[0:5]  # 取索引为0到4的字符，不包含索引为5的字符
print(result)  # Output: "Hello"

# 字符串查找
text = "Hello World"
result = text.find("World")  # 返回第一次出现"World"的位置
print(result)  # Output: 6

# 字符串替换
text = "Hello World"
result = text.replace("World", "Python")  # 将"World"替换成"Python"
print(result)  # Output: "Hello Python"