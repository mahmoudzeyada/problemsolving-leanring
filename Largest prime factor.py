#this my code but so dumb for large n
biggest = []
target = int(input())
r = 0


def is_prime(n):
    for i in range(2, n):
        if n % i == 0 and n != i:

            return False
    return True


for i in range(2, target):
    if target % i == 0:
        if (is_prime(i)):
            print(i)
