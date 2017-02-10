def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '*':
        return value1 * value2
    if operator == "/":
        return value1 / value2
    if operator == "-":
        return value1 - value2
    else:
        print ("Unrecognized Operator. Abort.")

#solution1
from operator import add, div, mul, sub


def basic_op(op, a, b):
    return {'+': add, '/': div, '*': mul, '-': sub}[op](a, b)

#solution2
def basic_op(operator, value1, value2):
    #take advantage of Python built in function, eval
    return eval( str(value1) + operator + str(value2) )
print basic_op('*', 5, 5)
print basic_op('+', 4, 7)
print basic_op('-', 15, 18)
print basic_op('/', 49, 7)