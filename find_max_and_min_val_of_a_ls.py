def min(arr):
    sort_array = sorted(arr)
    return sort_array[0]

def max(arr):
    sort_array = sorted(arr)
    return sort_array[-1]
arr = [4,6,2,1,9,63,-134,566]
print max(arr)
# Solution1
# def m(arr):
#     return min(arr)
#
# def m(arr):
#     return max(arr)