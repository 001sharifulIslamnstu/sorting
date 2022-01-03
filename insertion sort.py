dat = [int(dat) for dat in input().split()]

n = len(dat)

''' Insertion Sort '''
for i in range(1, n):
    for j in range(i, 0, -1):
        if dat[j - 1] > dat[j]:
            dat[j - 1], dat[j] = dat[j], dat[j - 1]
        else:
            break

print(*dat)
