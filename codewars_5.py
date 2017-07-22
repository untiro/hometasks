def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 1/(5/6/f(n-1)-1/6/f(n-2))

print(f(40))
