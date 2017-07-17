s = 'asa'
palindrom = True
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        palindrom = False
if palindrom:
    print(s, 'is a palindrom')
else:
    print(s, 'is not a palindrom')