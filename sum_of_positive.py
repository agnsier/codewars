# Sum positive int in array
def positive_sum(arr):
    empty_list = list()
    for x in arr:
        if x >= 0:
            empty_list.append(x)
        elif arr == []:
            return 0
    return sum(empty_list)

print positive_sum([1,-2,3,4,5])
print positive_sum([])
# Solution2
# def positive_sum(arr):
#   sum = 0
#   for e in arr:
#       if e > 0:
#           sum = sum + e
#   return sum
