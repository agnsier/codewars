def duty_free(price, discount, holiday_cost):
    savings = (discount/100) * price
    bootles = holiday_cost/savings
    return int(bootles)

#przykłady
def duty_free(price, discount, holiday_cost):
    save_money = price * discount/100
    if save_money == 0:
        return 0
    item = holiday_cost // save_money
    return item