def find_average(array):
    summing = sum(array)
    count = len(array)
    if array == []:
        return 0
    return (summing / count)