# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle


def find_needle(haystack):
    for i in haystack:
        if i == "needle":
            return "found the needle at position" ' %d' % haystack.index("needle")


print find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
#Solution1
#def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')
#Solution2
# def find_needle(haystack):
#     return ''.join("found the needle at position " + str(haystack.index("needle")))