

# def fact (n):
#     if n > 0 :
#         return fact(n-1)*n
#     else:
#         return 1
# print (fact(25))
from functools import reduce


def extraLongFactorials(n): return reduce(lambda x, y: x*y, range(1, n+1))


print(facto(55))
