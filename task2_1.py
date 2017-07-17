d = {}
l1 = [1, 2, 3, 4, 5, 6, 7, 2, 4]
l2 = ['q', 'w', 'e', 'r', 't', 'y', 'o']
for i in range(len(l1)):
    if l1[i] in d.keys():
        if i < len(l2):
            d[l1[i]]=d[l1[i]]+[l2[i]]
        else:
            d[l1[i]] = d[l1[i]] + [None]
    else:
        if i < len(l2):
            d[l1[i]]=[l2[i]]
        else:
            d[l1[i]] = [None]
for key, value in d.items():
    print(key, value)
