def count_substring(string, sub_string):
    count = 0
    f = 0
    for i in range(len(string)):
        f = string.find(sub_string, f)
        if f >= 0:
            count += 1
        else:
            break
        f += 1
    return count


print(count_substring("ininini", "ini"))
