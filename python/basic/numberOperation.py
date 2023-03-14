# 数字相加
a = 10
b = 5
result = a + b
print(result)  # Output: 15

# 数字相减
a = 10
b = 5
result = a - b
print(result)  # Output: 5

# 数字相乘
a = 10
b = 5
result = a * b
print(result)  # Output: 50

# 数字相除
a = 10
b = 5
result = a / b
print(result)  # Output: 2.0

# 取整除
a = 10
b = 3
result = a // b
print(result)  # Output: 3

# 取余数
a = 10
b = 3
result = a % b
print(result)  # Output: 1

# 数字的幂运算
a = 2
b = 3
result = a ** b
print(result)  # Output: 8

# 数字四舍五入
num = 3.1415926
result = round(num, 2)
print(result)  # Output: 3.14


import random

# 生成一个[0,1)之间的随机浮点数
random_float = random.random()
print(random_float)

# 生成一个指定范围内的随机整数
random_int = random.randint(1, 10)
print(random_int)

# 从一个序列中随机选择一个元素
seq = ["apple", "banana", "cherry"]
random_element = random.choice(seq)
print(random_element)

# 打乱一个序列中的元素
random.shuffle(seq)
print(seq)

# 生成一个符合正态分布的随机数
mu = 0  # 均值
sigma = 1  # 标准差
random_normal = random.normalvariate(mu, sigma)
print(random_normal)

# 生成一个符合指定参数的伽马分布的随机数
shape = 2  # 形状参数
scale = 1  # 尺度参数
random_gamma = random.gammavariate(shape, scale)
print(random_gamma)

# 生成一个符合指定参数的指数分布的随机数
lambda_param = 2  # 指数分布的λ参数
random_exponential = random.expovariate(lambda_param)
print(random_exponential)

# 生成一个符合指定参数的贝塔分布的随机数
alpha = 2  # β分布的α参数
beta = 3  # β分布的β参数
random_beta = random.betavariate(alpha, beta)
print(random_beta)