# #this my code but so dumb for large n
# biggest = []
# target = int(input())
# r = 0


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0 and n != i:

#             return False
#     return True


# for i in range(2, target):
#     if target % i == 0:
#         if (is_prime(i)):
#             print(i)
import math
n = 10000000000
factor=2
biggest_factor=0
max_factor=math.sqrt(n)
if  n  % 2==0:
    n=n/2
    while(n%2==0 and factor <=max_factor):
        n=n/2
        max_factor =math.sqrt(n)
    biggest_factor=factor
else:
    biggest_factor=0
factor=3
while n > 1 and factor <= max_factor:
    if n % factor ==0 :
        biggest_factor=factor
        n=n/factor
        while(n%factor==0):
            n=n/factor
            max_factor=math.sqrt(n)
    factor+=2
    
print (biggest_factor)