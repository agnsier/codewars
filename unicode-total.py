def uni_total(string):
    for ch in string:
        number = ord(ch)
    total = number +number
    return total

 #solution 1
def uni_total(string):
    return sum(map(ord, string))
#solution2
def uni_total(s):
    return sum(ord(c) for c in s)