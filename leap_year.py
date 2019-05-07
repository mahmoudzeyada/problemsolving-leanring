(lambda r: print(True) if r != 0 and r % 4 == 0 else print(False))((lambda s: 0 if s !=
                                                                    0 and s % 100 == 0 else s)(((lambda c: 0 if c % 400 == 0 else c)(int(input())))))
