def digitize(n):
    n = str(n)
    if n > 0:
        x = len(str(n))
        y = str(n)
        y = y[1:x]
        ls = list(y)
        ls = map(int, ls)
        ls.insert(0, 0)
        return ls
    else:
        y = int(str(n)[::-1])
        y = str(y)
        ls = list(y)
        ls = map(int, ls)
        return ls


print digitize(0348597)