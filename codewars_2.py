"""Sum of numbers from 0 to N"""

x = int(input())

if x < 0:
    print(x, '< ')
elif x == 0:
    print('0=0')
else:
    print('{0}={1}'.format('+'.join(str(e) for e in list(range(x+1))), str(sum(list(range(x+1))))))

