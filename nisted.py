if __name__ == '__main__':
    s = []
    n = []
    r = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n.append(name)
        s.append(score)
    min_score = min(s)
    v = max(s)-min_score
    min_r = 0
    count = 0
    flag = False

    # print(v)
    for j in s:
        if abs(j - min_score) <= v and j-min_score != 0:
            v = j - min_score

    for i in s:
        for j in range(len(s)):
            if abs(i-j) == v:
                r.append(n[j])
    for i in sorted(r):
        print(i)
