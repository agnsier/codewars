def double_char(s):
   return "".join([x * 2 for x in s])

print double_char("String")

# Solution1
# def double_char(s):
#     res = ''
#     for i in s:
#         res += i*2
#     return res