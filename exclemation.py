def remove(s):
    s = list(s)
    y = len(s) - 1
    e = "!"
    if  len(s) <= 0 :
        return ""
    if s[y] == e[0] :
        s[y] = ""
        without_exclamation = "".join(s)
        return without_exclamation
    else:
        return ''.join(s)
##solution1
def remove(s):
    if len(s) < 1:
       return s
    # s[-1] indexing last solution
    elif s[-1] == "!":
        return s[0: -1]
    else: return s
##solution2
def remove(s):
    return s[:-1] if s.endswith('!') else s
##solution3
def remove(s):
    import re
    if re.search('!$', s):
        s = s[:-1]
    return s

