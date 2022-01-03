dat = [int(dat) for dat in input().split()]

n = len(dat)

for i in range(n):
    min_index = i;
    for j in range(i + 1, n):
        if dat[min_index] > dat[j]:
            min_index = j
    dat[i], dat[min_index] = dat[min_index], dat[i]

print(*dat)
