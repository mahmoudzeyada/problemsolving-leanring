# if __name__ == '__main__':
#     nm = input().split()

#     n = int(nm[0])

#     m = int(nm[1])

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     k = int(input())

#     def sorting(arr, k):
#         for i in range(len(arr)):
#             for j in range(i+1, len(arr)):
#                 temp = arr[i]
#                 if temp[k] > arr[j][k]:
#                     arr[i] = arr[j]
#                     arr[j] = temp


#         return arr

#     for i in sorting(arr, k):
#         for j in i:
#             print(j, end=" ")
#         print("")


def sorting(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = arr[i]
            if temp[1] > arr[j][1]:
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print(sorting([("a", 1), ("b", 2), ("c", 1),
               ("d", 5), ("e", 11), ("f", 5), ("g", 9), ("h", 11)]))
