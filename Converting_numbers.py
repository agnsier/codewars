# Convert number to reversed array of digits
# Example 348597 => [7,9,5,8,4,3]


def digitize(n):
    if n > 0:
        y = int(str(n)[::-1])
        y = str(y)
        ls = list(y)
        ls = map(int, ls)
    if n < 0:
        x = len(str(n))
        y = str([-1, x-1])
        y = int(str(y))
        ls = list(y)
        ls = map(int, ls)
        ls.insert(0, 0)
    return ls

print digitize(-348597)