# Count sheeps if TRUE = 1
def count_sheeps(arrayOfSheeps):
    sum = 0
    for x in arrayOfSheeps:
        if x == False: continue
        elif arrayOfSheeps == None: return 1
        elif x == True:
            sum = sum + 1
    return sum
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
print count_sheeps(array1)
# Solution2 Counting just TRUE, TRUE = 1
# def count_sheeps(arrayOfSheeps):
# return arrayOfSheeps.count(True)