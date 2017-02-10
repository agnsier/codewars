# n - length of a array
def sum_array(arr):
    if arr is None:
        return 0
    else:
        arr = sorted(arr, key=int)
        return sum(arr[1:-1])

print sum_array([6, 2, 1, 8, 10])
print sum_array([6, 10])
print sum_array([])
# #Solution1
# def sum_array(arr):
#     return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0