import functools

print(functools.reduce(lambda char, reversed: char+reversed,
                       list(input()))
      )
