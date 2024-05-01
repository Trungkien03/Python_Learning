x = lambda a: a + 10
print(x(5))
# 15

x = lambda a, b: a * b
print(x(5, 6))
# 30

x = lambda a, b, c: a + b + c
print(x(5, 6, 7))
# 18

# lambda with if-else
x = lambda a: "Yes" if a % 2 == 0 else "No"
print(x(5))
# No

x = lambda a: "Yes" if a % 2 == 0 else "No"
print(x(6))
# Yes

# lambda with multiple statements
x = lambda a: (a + 10, a * 2)
print(x(5))
# (15, 10)

# lambda with default arguments
x = lambda a, b=10: a + b
print(x(5))
# 15

x = lambda a, b=10: a + b
print(x(5, 15))
# 20

# lambda with variable arguments
x = lambda *args: sum(args)
print(x(1, 2, 3, 4, 5))
# 15

x = lambda **kwargs: sum(kwargs.values())
print(x(a=1, b=2, c=3))
# 6

# lambda with filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
# [2, 4, 6, 8, 10]

# lambda with map
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# lambda with reduce
from functools import reduce