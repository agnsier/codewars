def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    result = list()
    negative_list = list()
    positive_list = list()

    for i in arr:
        if i > 0:
            positive_list.append(i)

        elif i < 0:
            negative_list.append(i)
    x = len(positive_list)
    y = sum(negative_list)
    result.append(x)
    result.append(y)
    return result


print count_positives_sum_negatives([])

# def count_positives_sum_negatives(arr):
#     if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#       if x > 0:
#           pos += 1
#       if x < 0:
#           neg += x
#     return [pos, neg]
#
# def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []