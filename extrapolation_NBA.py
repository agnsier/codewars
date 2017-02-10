def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        ppg = (float(ppg) * 48) / float(mpg)
        return round(ppg, 1)


print nba_extrap(10, 10)
print nba_extrap(30.8, 34.7)
print nba_extrap(0, 0)

# solution2
# def nba_extrap(ppg, mpg):
# return round(48 * ppg/float(mpg), 1) if mpg != 0 else 0.
