d, = {}
with open('access.log', 'r') as inf:
    for line in inf:
        line = line.strip().split()
        if line[0] in d.keys():
            d[line[0]] += 1
        else:
            d[line[0]] = 1
ds = sorted(d, key=d.get, reverse=True)
print(ds)
i = 0
for j in ds:
    if i < 10:
        print(j, 'sent', d[j], 'requests')
        i += 1
    else:
        break
