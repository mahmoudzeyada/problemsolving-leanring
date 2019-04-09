# import math

# # s = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"


# # def encryption(s):
# #     r = c = 0
# #     s = s.replace(" ", "")
# #     t = len(s)
# #     complete_str = ""
# #     grid = list()
# #     output_str = ""
# #     final = ""
# #     sqr = int(math.sqrt(t))
# #     if sqr**2 == t:
# #         r = c = sqr
# #     elif sqr * (sqr+1) >= t:
# #         r, c = sqr, sqr+1
# #     else:
# #         r = c = sqr+1
# #     print(t, c, r)

# #     complete_string_number = abs(t-r*c)
# #     if complete_string_number > 0:
# #         for i in range(complete_string_number):
# #             complete_str += "0"
# #     full_str = s+complete_str

# #     for i in range(r):
# #         subset_str = full_str[0:c]
# #         grid.append(subset_str)
# #         full_str = full_str[c:]
# #     for i in range(c):
# #         for j in range(r):
# #             output_str += grid[j][i]

# #     # if complete_string_number > 0:
# #     #     output_str = output_str.replace("0", "")
# #     for i in range(len(output_str)):

# #         if i % r == 0:
# #             final += output_str[0:r]+" "
# #             output_str = output_str[r:]
# #     return final.replace("0", "")


# # print(encryption(s))
# s = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"


# def encryption(s):
#     r = c = 0
#     s = s.replace(" ", "")
#     t = len(s)
#     complete_str = ""
#     grid = list()
#     output_str = ""
#     final = ""
#     sqr = int(math.sqrt(t))
#     if sqr**2 == t:
#         r = c = sqr
#     elif sqr * (sqr+1) >= t:
#         r, c = sqr, sqr+1
#     else:
#         r = c = sqr+1
#     print(t, c, r)

#     complete_string_number = abs(t-r*c)
#     if complete_string_number > 0:
#         for i in range(complete_string_number):
#             complete_str += "0"
#     full_str = s+complete_str

#     for i in range(r):
#         subset_str = full_str[0:c]
#         grid.append(subset_str)
#         full_str = full_str[c:]
#     for i in range(c):
#         for j in range(r):
#             output_str += grid[j][i]

#     # if complete_string_number > 0:
#     #     output_str = output_str.replace("0", "")
#     for i in range(len(output_str)):

#         if i % r == 0:
#             final += output_str[0:r]+" "
#             output_str = output_str[r:]
#     return final.replace("0", "")


# print(encryption(s))
# (lambda s: (lambda r: print(' '.join(map(lambda x: s[x::r], range(r)))))(int(-(-(len(s)**0.5)//1))))(input().strip())
# import sys
from math import ceil, sqrt


(lambda s: (lambda c: (print(' '.join(map(lambda x: s[x::c], range(c))))))(
    ceil(sqrt(len(s)))))(input().strip())
# this is fqin one line code
# (lambda s: ((lambda c: print(" ".join(map(lambda x: s[x::4], range(c)))))(
# int(-(-(len(s)**0.5)//1)))))(input().strip())
