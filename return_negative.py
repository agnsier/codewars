def make_negative( number ):
    if number > 0:
        return number*(-1)
    elif number <= 0:
        return number

print make_negative(-2)
print make_negative(9)
print make_negative(0)

# def make_negative( number ):
#     return -abs(number)